import tkinter
from tkinter import *
from Algorythm import *

def calulate_fun():
    equestion=entry_box.get()
    equestion = equestion.replace(" ", "")
    result=ODNN(list(equestion))
    equestion_tekst.set(equestion)
    result_tekst.set(result)


root = tkinter.Tk()

entry_box=Entry(root)

entry_box.pack()

calculate=Button(root,text="Oblicz",command=lambda:calulate_fun())
calculate.pack()

equestion_tekst=StringVar()
result_tekst=StringVar()

equestion = Label(root, textvariable=equestion_tekst, relief=RIDGE)
result=Label(root,textvariable=result_tekst,relief=RIDGE)

equestion.pack()
result.pack()


root.mainloop()