import tkinter
from tkinter import *
from tkinter import messagebox

root = tkinter.Tk()

#wczytywanie ciagow z pliku
ciag=open("Ciagi.txt",'r')
examples=ciag.read()
ciag.close()

sequence_table=str(examples).split('\n')#tablica z przykładami

#wyswietlacze
chain=StringVar()
result=StringVar()

etykieta = Label(root, textvariable=chain, relief=RIDGE)
#etykieta wyswietla wszytkie stany pośrednie(wszystkie kroki)
result_label=Label(root,textvariable=result,relief=RIDGE)

chain.set(str(sequence_table[0]))
result.set("tablica,stanow przejsciowych")

etykieta.pack()

ex = 0
#guziki funkcyjne
def next_sequence():
    sequence=sequence_table[ex]
    chain.set(str(sequence))
    ex=+1

step_by_step=Button(root,text="Krok po kroku")
run=Button(root,text="Automat")
next=Button(root,text="Następny ciąg", )
step_by_step.pack()
run.pack()
next.pack()

#guziki stanów mam już tablice obiektów
def state_disp():
    button_table=[]
    for i in range(0,20):
        button_table.append(Button(root,text="Q"+str(i),relief=FLAT))
        button_table[i].pack(side=LEFT)
    return button_table


state_disp()
result_label.pack(side=BOTTOM)
root.mainloop()
