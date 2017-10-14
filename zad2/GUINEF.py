import tkinter
from tkinter import *
import time
from tkinter import messagebox
#-----------------------------------------------Funkcje------------------------------------------------------------------
# tablice stanów
state_table = [
    [[0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9], [0, 10]],
    [11, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, 11, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, 11, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, 11, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, 11, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, 11, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, 11, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, 11, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, 11, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, 11],
    [11, 11, 11, 11, 11, 11, 11, 11, 11, 11]
]

line=''
index=0
step=[]
steps_table=[]
alphabet = "0123456789"
#-------------------------------------funkcje-----------------------------------------------------

#zmiana graficzna na przyciskach- funckja interakcja z GUI
def button_clear():
    for s in range(0, len(buttons)):
        buttons[s].configure(bg="white")

def state_change(state):
    global buttons
    global state_results

    state_results.append(state)
    button_clear()

    for item in state:
        if item==-1:
            pass
        else:
            if item==11:
                buttons[11].config(bg="green")
            else:
                buttons[item].config(bg="#FF0066")

    result.set("tablica,stanow przejsciowych:" + str(state_results))

# -------------------------fatyczny algorytm NFA--------------------------------------------
def NFA(element, prev_state):
    if element in alphabet:
        state = state_table[0][int(element)]+ [(state_table[prev_state][int(element)])]
    return state

#-----------------------------Button:automat ------------------------------------
def automat():
    if index<len(list(line)):
        state_change(NFA_cal_step(line))
        root.after(2000,automat)

#-----------------------------Button:step by step ------------------------------------
def NFA_cal_step(chain):
    global index
    global step
    global step_by_step
    global steps_table
    list_signs= list(chain)

    if index<len(list_signs):
        charter = list_signs[index]

        if index==0:
            state = state_table[0][int(charter)]
        else:
            state = NFA(charter, max(steps_table[index - 1]))

        step = state
        steps_table.append(state)

    index += 1
    if index==len(list_signs):
        step_by_step.configure(state=DISABLED)
    return step




#----------------------------------------------GUI------------------------------------------------------------
ex = 0
state_results=[]


root = tkinter.Tk()

#---------------------------------wczytywanie ciagow z pliku(nowa linia)---------------------
ciag=open("Ciagi.txt",'r')
examples=ciag.read()
ciag.close()

sequence_table=str(examples).split('\n')#tablica z przykładami

#-----------------------------------wyswietlacz------------------------------
chain=StringVar()
result=StringVar()

etykieta = Label(root, textvariable=chain, relief=RIDGE)
#etykieta wyswietla wszytkie stany pośrednie(wszystkie kroki)
result_label=Label(root,textvariable=result,relief=RIDGE)

chain.set("")
result.set("tablica,stanow przejsciowych:")


etykieta.pack()
result_label.pack(side=BOTTOM)


#--------------------------------------------nowa sekwencja pobieranie---------------------------------------
def next_sequence():
    del state_results[:]
    global ex
    # ex += 1
    if ex<len(sequence_table):
        sequence=sequence_table[ex]
        chain.set(str(sequence))
        ex += 1
    else:
        exit()

    return sequence

#---------------------------------------------Button: next Line-----------------------------------------

def next_line():
    global line
    line=next_sequence()
    global index
    global steps_table
    global step_by_step
    index=0
    steps_table=[]
    step_by_step.configure(state=ACTIVE)
    button_clear()
    result.set("tablica,stanow przejsciowych:" + str(steps_table))

#---------------------------------------------Buttons----------------------------------------------
step_by_step=Button(root,text="Krok po kroku",command=lambda:state_change(NFA_cal_step(line)))
auto=Button(root, text="Automat", command=lambda:automat())
next=Button(root,text=">>>", command=lambda:next_line())
step_by_step.pack()
auto.pack()
next.pack()


#----------------------------------------guziki stanow-create--------------------------------------
def state_disp():
    button_table=[]
    for i in range(0,12):
        button_table.append(Button(root,text="Q"+str(i),relief=RAISED))
        button_table[i].pack(side=LEFT)
    return button_table

buttons=state_disp()


root.mainloop()




#----------------------------------------------------------------------------------------------------------------------




