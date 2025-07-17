import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("이미지 테스트")

img = Image.open("./map_vertex_src/blueprint.jpg").convert("RGB")
tk_img = ImageTk.PhotoImage(img)

label = tk.Label(root, image=tk_img)
label.pack()

root.mainloop()
