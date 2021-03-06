from cProfile import label
from itertools import count
from pdb import Restart
import tkinter as tk
import maze_maker as mm
import time

def key_down(event):
    global key
    key = event.keysym
    print(key)

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx, cy, mx, my
    if key =="Up"     and maze_bg[my-1][mx] == 0: my -= 1
    if key =="Down"   and maze_bg[my+1][mx] == 0: my += 1
    if key =="Left"   and maze_bg[my][mx-1] == 0: mx -= 1
    if key =="Right"  and maze_bg[my][mx+1] == 0: mx += 1
    cx, cy = mx*100+50, my*100+50
    canvas.coords("tori", cx, cy)

    if key == "Return":            #Enterが押されたらウィンドウを消去する
        root.destroy()

    if cx == 1350 and cy == 750:   #こうかとんがゴール位置に到達した時
        global roop 
        label = tk.Label(text="GOAL",
                        font=("Times New Roman", 150),
                        fg="red"
                        )          #赤文字でGOALと表示させる
        label.place(x=500, y=300)
        maze.after_cancel(roop)    #リアルタイム処理を中断させる
        roop = None
        

    root.after(100, main_proc)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")

    canvas = tk.Canvas(root, width=1500, height=900, bg="black")
    canvas.pack()

    maze_bg = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_bg)

    canvas.create_rectangle(1300, 700, 1400, 800, fill="orange")  #左上にオレンジのスタート地点を配置する
    canvas.create_rectangle(100, 100, 200, 200, fill="green")     #右下に緑色のゴール位置を配置する

    tori = tk.PhotoImage(file="fig/9.png")
    mx, my = 1,1
    cx, cy = mx*100+50, my*100+50
    canvas.create_image(cx, cy, image=tori, tag="tori")

    key = ""
    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)

    main_proc()
    root.mainloop()