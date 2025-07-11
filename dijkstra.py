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
    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return isinstance(other, Vertex) and self.value == other.value

    def __lt__(self, other):  # heapq에서 비교 필요
        return self.value < other.value

    def __repr__(self):  # 디버깅용
        return f"Vertex({self.value})"


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
    path = []
    while len(queue):
        removed_distance, removed = queue.pop_task()
        visited[removed] = True

        # this piece of code is not part of the video, but it's useful to print the final path and distance
        if removed == end:
            while previous[removed]:
                path.append(removed.value)
                removed = previous[removed]
            path.append(start.value)
            print(f"shortest distance to {end.value}: ", distances[end])
            print(f"path to {end.value}: ", path[::-1])
            return

        for edge in graph.adjacency[removed]:
            if visited[edge.vertex]:
                continue
            new_distance = removed_distance + edge.distance
            if new_distance < distances[edge.vertex]:
                distances[edge.vertex] = new_distance
                previous[edge.vertex] = removed
                queue.add_task(new_distance, edge.vertex)
    return


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


# testing the algorithm
vertices = [Vertex("A"), Vertex("B"), Vertex("C"), Vertex("D")]
A, B, C, D = vertices

graph = Graph()
graph.add_edge(A, B, 1)
graph.add_edge(B, C, 1)
graph.add_edge(A, C, 1)
graph.add_edge(C, D, 1)

dijkstra(graph, start=A, end=D)