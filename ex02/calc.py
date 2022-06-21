import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("電卓")
#root.geometry("300x500")

def button_click(event):
    button = event.widget
    text = button["text"]
    entry.insert(tk.END, text)
    #tkm.showinfo(text, f"[{text}]のボタンがクリックされました")

entry = tk.Entry(root,
                justify="right", 
                width=10,
                font=("Times New Roman", 40)
                )
entry.grid(row=0, column=0, columnspan=3)

r, c , x= 1, 0 ,9
nums=[9, 8, 7, 6, 5, 4, 3, 2, 1, 0, "+"]
for i in nums:
    button = tk.Button (root,
                        font=("Times New Roman", 30),
                        text=i,
                        width=4, height=2
                        )
    button.bind("<1>", button_click)
    button.grid(row=r, column=c)

    c+=1
    x-=1
    if (x)%3 == 0:
        r += 1
        c = 0


root.mainloop()