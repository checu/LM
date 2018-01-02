import tkinter
from tkinter import *
from Algorythm import S

def calulate_fun():

    expresion=entry_box.get()
    result=S(expresion)
    if result ==1:
        result_tekst.set("True")
    else:
        result_tekst.set("False")
    equestion_tekst.set(expresion)



root = tkinter.Tk()
root.geometry("300x200")
root.configure(background='yellow')

entry_box=Entry(root)

entry_box.place(x=50, y= 35)

calculate=Button(root,text="Execute",command=lambda:calulate_fun())
calculate.place(x=200, y=34)

equestion_tekst=StringVar()
result_tekst=StringVar()

equestion = Label(root, textvariable=equestion_tekst, relief=RIDGE)
equestion_label=Label(root, text="Expression", relief=RIDGE)
result=Label(root,textvariable=result_tekst,relief=RIDGE)
title_label=Label(root, text="Syntax analyzer", relief=RIDGE)
result_label=Label(root, text="Result", relief=RIDGE)

equestion.place(x=150,y=70)
equestion_label.place(x=50,y=70)
result_label.place(x=50, y=110)
title_label.place(x=0,y=0)
result.place(x=150,y=110)


root.mainloop()