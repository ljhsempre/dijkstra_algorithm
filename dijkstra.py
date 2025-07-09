import sys
from heapq import heapify, heappush, heappop

def dijkstra(graph, src, dest):
    inf = sys.maxsize                              # infinite value
    node_data = {
        'A':{'cost':inf, 'pred':[]},
        'B':{'cost':inf, 'pred':[]},
        'C':{'cost':inf, 'pred':[]},
        'D':{'cost':inf, 'pred':[]},
        'E':{'cost':inf, 'pred':[]},
        'F':{'cost':inf, 'pred':[]}
    }
    node_data[src]['cost'] = 0                     # Making the value of starting point zero
    visited = []
    temp = src
    for i in range(5):                             # why 5?, n(vertices) : n => n-1 steps
        if temp not in visited:
            visited.append(temp)                   # append : adding new value at the end of the list
            min_heap = []
            for j in graph[temp]:
                if j not in visited:
                    cost = node_data[temp]['cost'] + graph[temp][j]             # cost(c) = cost(b) + distance(b->c)
                    if cost < node_data[j]['cost']:
                        node_data[j]['cost'] = cost
                        node_data[j]['pred'] = node_data[temp]['pred'] + list(temp)      # 딕셔너리 -> 리스트 : 키만 남음 ['A', 'B']
                    heappush(min_heap, (node_data[j]['cost'], j))
                    print(min_heap)
        heapify(min_heap)
        temp = min_heap[0][1]
        print('Shortest Distance: ' + str(node_data[dest]['cost']))
        print('Shortest Path: ' + str(node_data[dest]['pred'] + list(dest)))

if __name__ == "__main__":
    graph = {
        'A' : {'B':2, 'C':4},
        'B' : {'A':2, 'C':3, 'D':8}, 
        'C' : {'A':4, 'B':3, 'D':2, 'E':5},
        'D' : {'B':8, 'C':2, 'E':11, 'F':22},
        'E' : {'C':5, 'D':11, 'F':1},
        'F' : {'D':22, 'E':1}
    }

    source = 'A'
    destination = 'F'
    dijkstra(graph, source, destination)