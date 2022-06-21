import tkinter as tk
import tkinter.messagebox as tkm
 
bg = tk.Tk()

bg.geometry('300x500')

bg.title('calculater')

def buttons(num):
    a = tk.Button(bg,text=f"{num}",font=("Times New Roman",30),
                width=4,height=2,command=lambda:coma(num))
    return a

def coma(n):
    tkm.showinfo("",f"{n}のボタンがクリックされました")


button1 = buttons(1)
button2 = buttons(2)
button3 = buttons(3)
button4 = buttons(4)
button5 = buttons(5)
button6 = buttons(6)
button7 = buttons(7)
button8 = buttons(8)
button9 = buttons(9)
button0 = buttons(0)


button1.grid(row=3,column=3)
button2.grid(row=3,column=2)
button3.grid(row=3,column=1)
button4.grid(row=2,column=3)
button5.grid(row=2,column=2)
button6.grid(row=2,column=1)
button7.grid(row=1,column=3)
button8.grid(row=1,column=2)
button9.grid(row=1,column=1)
button0.grid(row=4,column=1,)


bg.mainloop()