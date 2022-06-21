import tkinter as tk
import tkinter.messagebox as tkm


root = tk.Tk()
root.title("電卓")
#root.geometry("300x500")


def button_click(event):      #各ボタンが押された時の処理
    button = event.widget
    text = button["text"]
    #tkm.showinfo(text, f"[{text}]のボタンがクリックされました")

    try:
        if text == "=":           #=が押されたら計算結果をentry2に表示する
            eqn = entry1.get()
            ans = (eval(eqn))
            entry2.delete(0,tk.END)
            entry2.insert(tk.END, ans)
        elif text == "AC":        #ACが押されたら数字を全て消す
            entry1.delete(0,tk.END)
            entry2.delete(0,tk.END)
        elif text == "C":         #Cが押されたら数字を一桁消す
            entry1.delete(len(entry1.get())-1, tk.END)
        elif text in ["+", "-", "*", "/"]:         #符号を入力したら
            if entry1.get()[-1] in ["+", "-", "*", "/"]:    #最後尾が符号だった時に
                entry1.delete(len(entry1.get())-1, tk.END)
                entry1.insert(tk.END, text)        #符号を置き換える
            else:
                entry1.insert(tk.END, text)        #最後尾が符号でなければそのまま入力する
        else:                     #数字を入力する
            entry1.insert(tk.END, text)
    except:                       #式として成り立たない時はERRORを返す
            entry2.delete(0,tk.END)
            entry2.insert(tk.END, "ERROR")


entry1 = tk.Entry(root,        #数式を入力するテキストボックス1を配置する
                justify="right", 
                width=10,
                font=("Times New Roman", 40)
                )
entry1.grid(row=0, column=0, columnspan=4)

entry2 = tk.Entry(root,        #計算結果が出力されるテキストボックス2を配置する
                justify="right", 
                width=10,
                font=("Times New Roman", 40)
                )
entry2.grid(row=1, column=0, columnspan=4)


r, c , x= 2, 0 ,0
nums=["",  "AC", "C", "/", 9, 8, 7, "*", 6, 5, 4,"-", 3, 2, 1, "+", 0, "", "", "="]
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
    if (x)%4 == 0:
        r += 1
        c = 0


root.mainloop()