from dijkstra_module import Graph,Vertex, dijkstra
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import math

# 클릭 좌표 저장
points = []
vertices = []
coord_map = {}


# 클릭 이벤트 핸들러
def on_click(event):
    x, y = event.x, event.y
    print(f'정점 클릭 위치: ({x}, {y})')

    point_name = chr(65 + len(points))
    vertex = Vertex(point_name)

    # 저장
    points.append((x, y))
    vertices.append(vertex)
    coord_map[vertex.name] = (x, y)

    # 시각화
    canvas.create_oval(x-8, y-8, x+8, y+8, fill='red')
    canvas.create_text(x, y-15, text=point_name, fill='blue', font=('Arial', 14, "bold"))


# 이미지 선택 및 Tkinter 초기화
root = tk.Tk()
root.title('도면 위 클릭으로 정점 지정')

# 이미지 선택
file_path = filedialog.askopenfilename(title='도면 이미지 선택')
image = Image.open(file_path).convert('RGB')
tk_image = ImageTk.PhotoImage(image)

# 캔버스에 이미지 표시
canvas = tk.Canvas(root, width=image.width, height=image.height)
canvas.pack()
canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
canvas.bind('<Button-1>', on_click)


# 두 점 사이 유클리디안 거리 계산
def euclidean(p1, p2):
    return math.dist(p1, p2)


# 키보드로 경로 계산
def compute_path(event):
    if len(vertices) < 2:
        print('정점이 두 개 이상 필요합니다.')
        return
    
    # 그래프 생성
    graph = Graph()
    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if i != j:
                dist = math.dist(points[i], points[j])
                graph.add_edge(vertices[i], vertices[j], dist)

    # 최단 경로 탐색 및 시각화
    start = vertices[0]  # 시작 정점 (예: A)
    end = vertices[-1]   # 도착 정점 (예: C)
    path, distance = dijkstra(graph, start, end)

    print("최단 경로:", [v.name for v in path])
    print("총 거리:", distance)

    # 경로 선 그리기
    for i in range(len(path) - 1):
        x1, y1 = coord_map[path[i].name]
        x2, y2 = coord_map[path[i + 1].name]
        canvas.create_line(x1, y1, x2, y2, fill="blue", width=3)

# Enter 키 눌렀을 때 경로 계산
root.bind('<Return>', compute_path)

root.mainloop()
