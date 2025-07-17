import itertools
from heapq import heappush, heappop


class Graph:
    def __init__(self):
        self.adjacency = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adjacency:
            self.adjacency[vertex] = []
    
    def add_edge(self, from_vertex, to_vertex, distance):
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        self.adjacency[from_vertex].append(Edge(distance, to_vertex))

class Vertex:
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return isinstance(other, Vertex) and self.name == other.name

    def __lt__(self, other):  # heapq에서 비교 필요
        return self.name < other.name

    def __repr__(self):  # 디버깅용
        return f"Vertex({self.name})"


class Edge:
    def __init__(self, distance, vertex):
        self.distance = distance
        self.vertex = vertex


def dijkstra(graph, start, end):
    previous = {v: None for v in graph.adjacency.keys()}
    visited = {v: False for v in graph.adjacency.keys()}
    distances = {v: float("inf") for v in graph.adjacency.keys()}
    distances[start] = 0
    queue = PriorityQueue()
    queue.add_task(0, start)

    while len(queue):
        removed_distance, removed = queue.pop_task()
        visited[removed] = True

        # this piece of code is not part of the video, but it's useful to print the final path and distance
        if removed == end:
            break

        for edge in graph.adjacency[removed]:
            if visited[edge.vertex]:
                continue
            new_distance = removed_distance + edge.distance
            if new_distance < distances[edge.vertex]:
                distances[edge.vertex] = new_distance
                previous[edge.vertex] = removed
                queue.add_task(new_distance, edge.vertex)
    path = []
    current = end
    while current:
        path.append(current)
        current = previous[current]
    path.reverse()

    return path, distances[end]


# slightly modified heapq implementation from https://docs.python.org/3/library/heapq.html
class PriorityQueue:
    def __init__(self):
        self.pq = []  # list of entries arranged in a heap
        self.entry_finder = {}  # mapping of tasks to entries
        self.counter = itertools.count()  # unique sequence count

    def __len__(self):
        return len(self.pq)

    def add_task(self, priority, task):
        'Add a new task or update the priority of an existing task'
        if task in self.entry_finder:
            self.update_priority(priority, task)
            return self
        count = next(self.counter)
        entry = [priority, count, task]
        self.entry_finder[task] = entry
        heappush(self.pq, entry)

    def update_priority(self, priority, task):
        'Update the priority of a task in place'
        entry = self.entry_finder[task]
        count = next(self.counter)
        entry[0], entry[1] = priority, count

    def pop_task(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            priority, count, task = heappop(self.pq)
            del self.entry_finder[task]
            return priority, task
        raise KeyError('pop from an empty priority queue')

# 테스트용 CLI (원하면 유지)
if __name__ == "__main__":
    vA = Vertex("A")
    vB = Vertex("B")
    vC = Vertex("C")
    graph = Graph()
    graph.add_edge(vA, vB, 5)
    graph.add_edge(vB, vC, 3)
    graph.add_edge(vA, vC, 10)

    path, dist = dijkstra(graph, vA, vC)
    print("최단 경로:", [v.name for v in path])
    print("거리:", dist)