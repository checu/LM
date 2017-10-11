import tkinter
from tkinter import *
from tkinter import messagebox

root = tkinter.Tk()
chain=StringVar()

etykieta = Label( root, textvariable=chain, relief=RIDGE )

chain.set("Hey!? How are you doing?")
etykieta.pack()

#guziki funkcyjne
step_by_step=Button(root,text="Krok po kroku")
run=Button(root,text="Automat")
step_by_step.pack()
run.pack()

#guziki stanów

for i in range(0,20):
    state=Button(root,text="Q"+str(i),relief=FLAT)
    state.pack(side=LEFT)


root.mainloop()
