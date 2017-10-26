import tkinter
from tkinter import *
from Algorythm import *


root = tkinter.Tk()
root.geometry("320x400")
root.configure(background='#BABABA')

frame_film=Frame(root, width=320, height=50, background="#646464", relief='groove',bd=2)
frame_film.place(x=0,y=88)

canvas_width = 320
canvas_height =88


triangle = Canvas(root,width=canvas_width,height=canvas_height,background='#BABABA',bd=0)
triangle.pack()

points = [20,60,40,60,30,85]
triangle.create_polygon(points, fill='black', width=5)

title=Label(root,text="Maszyna Turinga- zwiekszanie liczby rzeczysiwstej o 3",relief='groove')
title.place(x=17,y=0)

def tape_disp():
    tape_table=[]
    for i in range(0,16):
        tape_table.append(Button(root,text="#",relief=GROOVE))
        tape_table[i].place(x=2+i*20,y=100)

    return tape_table

tape=tape_disp()

def state_disp():
    button_table=[]
    for i in range(0,12):
        button_table.append(Button(root,text="Q"+str(i),relief=RAISED))
        button_table[i].pack(side=LEFT)
    return button_table

buttons=state_disp()

root.mainloop()