import tkinter as tk
import tkinter.messagebox as tkm


root = tk.Tk()
root.title("電卓")
#root.geometry("300x500")


def button_click(event):      #各ボタンが押された時の処理
    button = event.widget
    text = button["text"]
    #tkm.showinfo(text, f"[{text}]のボタンがクリックされました")

    if text == "=":           #=が押されたら計算結果を表示する
        eqn = entry.get()
        ans = int(eval(eqn))
        entry.delete(0,tk.END)
        entry.insert(tk.END, ans)
    elif text == "AC":        #ACが押されたら数字を全て消す
        entry.delete(0,tk.END)
    elif text == "C":         #Cが押されたら数字を一桁消す
        entry.delete(len(entry.get())-1, tk.END)
    else:                     #数字か符号を入力する
        entry.insert(tk.END, text)


entry = tk.Entry(root,        #テキストボックスを配置する
                justify="right", 
                width=10,
                font=("Times New Roman", 40)
                )
entry.grid(row=0, column=0, columnspan=3)


r, c , x= 1, 0 ,9
nums=["", "AC", "C", 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, "+", "-", "*", "/", "="]
#各ボタンを配置する
for i in nums:
    button = tk.Button (root,
                        font=("Times New Roman", 30),
                        text=i,
                        width=4, height=1
                        )
    button.bind("<1>", button_click)
    button.grid(row=r, column=c)

    c+=1
    x-=1
    if (x)%3 == 0:
        r += 1
        c = 0


root.mainloop()