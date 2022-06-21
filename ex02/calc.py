from cgitb import text
import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("電卓")
root.geometry("300x500")

def button_click(event):
    button = event.widget
    text = button["text"]
    tkm.showinfo(text, f"[{text}]のボタンがクリックされました")

r, c = 0, 0
for i in range (9, -1, -1):
    button = tk.Button (root,
                        font=("Times New Roman", 30),
                        text=i,
                        width=4, height=2)

    button.bind("<1>", button_click)
    button.grid(row=r, column=c)
    c+=1
    if (i-1)%3 == 0:
        r += 1
        c = 0

root.mainloop()