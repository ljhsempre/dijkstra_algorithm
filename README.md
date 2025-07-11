# dijkstra_algorithm

다익스트라 알고리즘 연습 및 비상 상황 시 건축물 내에서 최단 거리의 탈출 경로를 찾는 다익스트라 알고리즘 구현
Dijkstra Algorithm practice & Developing Dijkstra algorithm that finds a shortest path to evacuate in a building when emergency

---

## 구현 목표

### I. 1차 목표

0. 다익스트라 알고리즘의 이론을 이해하고 예제를 통해 파이썬으로 구현하는 방법을 이해한다. ✅
1. 구조는 이해했으나 유튜브 예제에 나온 특정한 자료값에서만 이를 구현할 수 있는데, 일반적 상황에서도 그에 맞는 최단 경로를 찾는 코드를 작성해야함.
2. 사용자가 노드를 지정했을 때 그 상황에 맞는 최단 경로를 찾는 알고리즘 구현

### II. 2차 목표

1. 사용자가 건축물의 도면을 불러오게 하는 기능 구현
2. 사용자가 건축물의 도면에서 노드를 지정할 수 있게 하는 기능 구현

- 이 과정에서의 문제는 사용자가 노드를 지정하고 각 노드들을 연결하여 최단 거리를 구하였을 때 그 경로에 벽과 같은 장애물이 가로막는 경우도 생각해야함.
- 직선 경로를 사용할 수 없는 경우에는 중간 노드를 지정하는 추가적인 단계가 필요함.

3. 사용자가 지정한 노드들을 이어 최단 경로를 탐색하고 그 최단 경로를 도면 상에 표시함.

- 하지만 현실에서의 건축물은 단층이 아닌 다층인 구조가 많으므로 가능하다면 여러 층을 이을 수 있는 기능을 구현한다.

### III. 3차 목표

1. 사용자 화면(프론트엔드)를 다듬기.

#### 우선적 목표는 2주 내로 1차 목표는 구현하고 2차 목표는 1번에서 2번까지 구현하는 것이 목표임.

---

## 2025. 7. 9.

> ex_dijkstra.py
> [참조한 유튜브 영상 링크 - [7.5] Dijkstra Shortest Path Algorithm in Python - ThinkX Academy](https://www.youtube.com/watch?v=OrJ004Wid4o)

```python
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
```

`__main__`의 의미는 직접 실행될 때만 이 코드를 실행하라는 뜻

---

## 2025. 7. 11.

> dijkstra.py
> [참조한 유튜브 영상 링크 - Dijkstra's Algorithm - A step by step analysis, with sample Python code - Glassbyte ](https://www.youtube.com/watch?v=_B5cx-WD5EA&t=44s) > [코드와 이미지 자료는 유튜브 영상을 통해 얻었습니다.]

이 영상에서는 이전 영상의 예제와는 다른 방법을 사용한다.
먼저 distance, previous, visited의 변수를 지정한다.
![변수 지정](./md_src/graph.png)

그 후 adjacency_list를 딕셔너리 자료형으로 인접한 노드에 대한 정보를 입력받는다.
![adjacency_list](./md_src/logic.png)

앞서 언급되었던 heapq 라이브러리를 직접 구현하여 살짝 수정한 유사한 기능을 가진 PriorityQueue를 도입해 우선순위를 결정한다.
(사실 무슨 의미인지는 대략 알겠지만 설명하는 것이 너무 힘드니 첨부 사진을 붙이겠다.)
![overall logic](./md_src/overall.png)
