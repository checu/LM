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
root.geometry("300x200")
root.configure(background='#3a78a8')

entry_box=Entry(root)

entry_box.place(x=50, y= 25)

calculate=Button(root,text="Oblicz",command=lambda:calulate_fun())
calculate.place(x=200, y=24)

equestion_tekst=StringVar()
result_tekst=StringVar()

equestion = Label(root, textvariable=equestion_tekst, relief=RIDGE)
equestion_label=Label(root, text="Rownanie ONP", relief=RIDGE)
result=Label(root,textvariable=result_tekst,relief=RIDGE)
result_label=Label(root, text="Wynik", relief=RIDGE)

equestion.place(x=150,y=60)
equestion_label.place(x=50,y=60)
result_label.place(x=50, y=100)
result.place(x=150,y=100)


root.mainloop()