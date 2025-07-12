import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def on_click(event):
    x, y = event.x, event.y
    print(f'정점 클릭 위치: ({x}, {y})')
    print(f"canvas 존재 여부: {canvas.winfo_exists()}")

    try:
        oval_id = canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill="red", outline="black", width=2)
        text_id = canvas.create_text(x, y - 15, text="★", fill="blue", font=("Arial", 16, "bold"))
        canvas.tag_raise(oval_id)  # 혹시 이미지 위에 안 뜰까봐
        canvas.tag_raise(text_id)
        print("⭕ 도형 그림 성공")
    except Exception as e:
        print("❌ 오류:", e)
    points.append((x, y))

points = []

root = tk.Tk()
root.title('도면 위 클릭으로 정점 지정')


# 이미지 선택
file_path = filedialog.askopenfilename(title='도면 이미지 선택')
image = Image.open(file_path)
image = image.convert('RGB')
images = []

global tk_image
tk_image = ImageTk.PhotoImage(image)
images.append(tk_image)

# 캔버스에 이미지 표시
canvas = tk.Canvas(root, width=image.width, height=image.height)
canvas.pack()

image_id = canvas.create_image(0,0, anchor=tk.NW, image=tk_image)
canvas.tag_lower(image_id)

# 클릭 이벤트 바인딩
canvas.bind("<Button-1>", on_click)
canvas.create_rectangle(0, 0, image.width, image.height, outline="red")

root.mainloop()

print('이미지 크기:', image.size)
print('이미지 모드: ', image.mode)
print('모든 클릭 좌표:', points)