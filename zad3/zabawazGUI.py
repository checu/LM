import tkinter
from tkinter import *

# maszyna Turinga: "+3" do liczby rzeczywistej

alphabet ="-123456789"
points = [0,60,20,60,10,85]

state_table=[
            [[0,"","P"],[2,"","P"],[1,"","P"],[1,"","P"],[1,"","P"],[1,"","P"],[1,"","P"],[1,"","P"],[1,"","P"],[1,"","P"],[1,"","P"],[1,"","P"]],
            [[3,"","L"],[1,"","P"],[1,"","P"],[1,"","P"],[1,"","P"],[1,"","P"],[1,"","P"],[1,"","P"],[1,"","P"],[1,"","P"],[1,"","P"],[1,"","P"]],
            [[4,"","L"],[2,"","P"],[2,"","P"],[2,"","P"],[2,"","P"],[2,"","P"],[2,"","P"],[2,"","P"],[2,"","P"],[2,"","P"],[2,"","P"],[2,"","P"]],
            [[-1,"",""],[-1,"",""],[10,"3",""],[10,"4",""],[10,"5",""],[10,"6",""],[10,"7",""],[10,"8",""],[10,"9",""],[5,"0","L"],[5,"1","L"],[5,"2","L"]],
            [[-1,"",""],[-1,"",""],[6,"7","L"],[6,"8","L"],[6,"9","L"],[10,"0",""],[10,"1",""],[10,"2",""],[10,"3",""],[10,"4",""],[10,"5",""],[10,"6",""]],
            [[10,"1",""],[-1,"",""],[10,"1",""],[10,"2",""],[10,"3",""],[10,"4",""],[10,"5",""],[10,"6",""],[10,"7",""],[10,"8",""],[10,"9",""],[5,"0","L"]],
            [[-1,"",""],[9,"#","P"],[6,"9","L"],[7,"0","L"],[10,"1",""],[10,"2",""],[10,"3",""],[10,"4",""],[10,"5",""],[10,"6",""],[10,"7",""],[10,"8",""]],
            [[-1,"",""],[8,"#","P"],[10,"",""],[10,"",""],[10,"",""],[10,"",""],[10,"",""],[10,"",""],[10,"",""],[10,"",""],[10,"",""],[10,"",""]],
            [[-1,"",""],[-1,"",""],[10,"-",""],[-1,"",""],[-1,"",""],[-1,"",""],[-1,"",""],[-1,"",""],[-1,"",""],[-1,"",""],[-1,"",""],[-1,"",""]],
            [[-1,"",""],[-1,"",""],[-1,"",""],[-1,"",""],[-1,"",""],[-1,"",""],[-1,"",""],[-1,"",""],[-1,"",""],[10,"3",""],[10,"2",""],[10,"1",""]],
            [[],[],[],[],[],[],[],[],[],[],[],[]]
             ]

def button_clear():
    global buttons
    for s in range(0, len(buttons)):
        buttons[s].configure(bg="white")

def state_change(state):# przesunięcie glowicy prawo lewo, aktualny stan Q ina label i update taśmy
    global buttons
    global tape
    global points
    button_clear()
    tape_disp(tape)
    state_value.set("Aktualny stan:"+str(state))
    if state[0]==-1:
        buttons[11].config(bg="#9F303E")
    elif state[0]==10:
        buttons[10].config(bg="#A2CFB7")
    else:
        buttons[state[0]].config(bg="#CDB5C4")
    if state[2]=="P":
        triangle.move(tom,20,0)
    if state[2]=="L":
        triangle.move(tom, -20, 0)


def auto():
    if state[0] != 10:
        state_change(Turing_Machine(charters))
        root.after(1000, auto)


tape=[]

#dane wejsciowe
chain = open("ciagi.txt", 'r')
chains = chain.read()
chain.close()
sequences = str(chains).split('\n')

start = 0
#turing

tape=[]
index = 0
charters=sequences[index]
tape=list(charters)
state=state_table[0][0]
lista=[]

def Turing_Machine(sequence):
    global index
    global start
    global state
    charter=tape[index]

    if charter == "#":
        charter = -2
    elif charter == "-":
        charter = -1

    if start==0:
        state = state_table[0][int(charter)+2]
    else:
        state=state_table[state[0]][int(charter)+2]

        if state[1]!="":
            tape[index]=state[1]

    if state[2] == "P":
        index += 1
    elif state[2] == "L":
        index -= 1
    start+=1
    lista.append(state)
    print(state)
    print(tape)

    return state
    print(lista)





#----------------------------------------------GUI--------------------------------------------------------
root = tkinter.Tk()
root.geometry("320x400")
root.configure(background='#F0FFF0')

frame_film=Frame(root, width=320, height=50, background="#236666", relief='groove',bd=2)
frame_film.place(x=0,y=88)

canvas_width = 320
canvas_height =88

#-------------------------trojkat mocy;p----------------------------
triangle = Canvas(root,width=canvas_width,height=canvas_height,background='#F0FFF0',bd=0)
triangle.pack()

# points = [20,60,40,60,30,85]
tom=triangle.create_polygon(points, fill='black', width=5)

title=Label(root,text="Maszyna Turinga- zwiekszanie liczby rzeczysiwstej o 3",relief='groove')
title.place(x=17,y=0)

state_value=StringVar()
state_value_label=Label(root,textvariable=state_value,relief="ridge")
state_value_label.place(x=140,y=153)

state_value.set("Aktualny stan:")

start_button=Button(root,text="START",command=lambda:auto())
start_button.place(x=30,y= 150)

def tape_disp(chain):
    #global sequences
    tape_value=chain
    tape_table=[]
    for i in range(0,16):
        if i<len(tape_value):
            tape_table.append(Button(root,text=str(tape_value[i]),relief=GROOVE))
        else:
            tape_table.append(Button(root, text="#", relief=GROOVE))
        tape_table[i].place(x=2+i*20,y=100)

    return tape_table

tapeL=tape_disp(sequences[0])

def state_disp():
    button_table=[]
    for i in range(0,12):
        button_table.append(Button(root,text="Q"+str(i),relief=GROOVE))
        button_table[i].pack(side=LEFT)
    return button_table

buttons=state_disp()



root.mainloop()

# Turing_Machine(sequences)