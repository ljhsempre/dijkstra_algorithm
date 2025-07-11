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
    path = []
    while len(queue):
        removed_distance, removed = queue.pop_task()
        visited[removed] = True

        # this piece of code is not part of the video, but it's useful to print the final path and distance
        if removed == end:
            while previous[removed]:
                path.append(removed.name)
                removed = previous[removed]
            path.append(start.name)
            print(f"shortest distance to {end.name}: ", distances[end])
            print(f"path to {end.name}: ", path[::-1])
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

# 그래프 생성
graph = Graph()
name_to_vertex = {}

while True:
    node_name = input('정점 이름을 입력하세요. (끝내려면 빈칸): ').strip() # strip(): 문자열 처리에서 불필요한 공백이나 줄바꿈을 없애는 함수.
    if node_name == "":
        break
    if node_name not in name_to_vertex:
        name_to_vertex[node_name] = Vertex(node_name)
    from_vertex = name_to_vertex[node_name]

    while True:
        adjacent_info = input(f'{node_name}에 인접한 정점과 거리 (예 : D 4), (없으면 빈칸): ')
        if adjacent_info == '':
            break
        try:     # try-except 구문: 에러가 날 수 있는 코드를 안전하게 실행하기 위한 예외 처리 도구: 에러가 나더라도 그냥 프로그램 속행하라
            neighbor_name, dist = adjacent_info.split() # split(): 문자열을 공백을 기준으로 나누어서 리스트로 처리하는 함수
            dist = float(dist)
        except ValueError:
            print('형식이 잘못되었습니다. 다시 입력해주세요.')
            continue

        if neighbor_name not in name_to_vertex:
            name_to_vertex[neighbor_name] = Vertex(neighbor_name)
        to_vertex = name_to_vertex[neighbor_name]

        graph.add_edge(from_vertex, to_vertex, dist)

# 이름 -> Vertex 매핑
name_to_vertex = {v.name: v for v in graph.adjacency.keys()}

# 사용자 입력
print('입력한 정점은 다음과 같습니다.')
for vertex in graph.adjacency.keys():
    print(vertex.name,end=" ")
print('')
start_name = input("시작 정점의 이름을 입력하세요: ")
end_name = input("도착 정점의 이름을 입력하세요: ")

# 유효성 검사
if start_name not in name_to_vertex or end_name not in name_to_vertex:
    print("잘못된 정점 이름입니다.")
else:
    start = name_to_vertex[start_name]
    end = name_to_vertex[end_name]
    dijkstra(graph, start, end)