# dijkstra_algorithm

다익스트라 알고리즘 연습 및 비상 상황 시 건축물 내에서 최단 거리의 탈출 경로를 찾는 다익스트라 알고리즘 구현
Dijkstra Algorithm practice & Developing Dijkstra algorithm that finds a shortest path to evacuate in a building when emergency

# 2025. 7. 9.

[참조](https://www.youtube.com/watch?v=OrJ004Wid4o)
`if **name** == "**main**":
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
    dijkstra(graph, source, destination)`

`__main__`의 의미는 직접 실행될 때만 이 코드를 실행하라는 뜻
