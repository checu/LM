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

# wczytywanie ciagow z pliku
ciag = open("Ciagi.txt", 'r')
examples = ciag.read()
ciag.close()

sequence_table = str(examples).split('\n')

# print(sequence_table)
alphabet = "0123456789"
def state_change(state):
    global buttons
    global state_results
    global lp
    state_results.append(state)
    for s in range(0, len(buttons)):
        buttons[s].configure(bg="white")
    for item in state:
        if item==-1:
            pass
        else:
            buttons[item].config(bg="#FF0066")


    result.set("tablica,stanow przejsciowych:" + str(state_results))

# funckjaliczaca
def NFA(element, prev_state):
    if element in alphabet:
        state = state_table[0][int(element)]+ [(state_table[prev_state][int(element)])]
    return state


# funkcja przetwarzajaca:
def NFA_cal(sequence):
    steps_table = []
    elements = list(sequence)
    index = 0
    for element in elements:
        #time.sleep(0.2)
        index += 1
        if index == 1:
            state = state_table[0][int(element)]
        else:
            state = NFA(element, max(steps_table[index-2]))

        result.set("aktualny stan:" + str(state))
        state_change(state)
        steps_table.append(state)
    return steps_table
#-----------------------------step by step ------------------------------------
line=''
lp=0
step=[]
steps_table=[]

def NFA_cal_step(digit):
    global lp
    global step
    cos= list(digit)
    global steps_table
    if lp<len(cos):
        charter = cos[lp]
        if lp==0:
            state = state_table[0][int(charter)]
        else:
            state = NFA(charter, max(steps_table[lp-1]))
        result.set("aktualny stan:" + str(state))
        step = state
        steps_table.append(state)
        
    else:
        next.config(state=DISABLED)
    lp += 1
    return step




#----------------------------------------------Koniec funkcji------------------------------------------------------------

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

chain.set("")
result.set("tablica,stanow przejsciowych:")


etykieta.pack()
result_label.pack(side=BOTTOM)

ex = 0
state_results=[]
#guziki funkcyjne
def next_sequence():
    del state_results[:]
    global ex
    ex += 1
    if ex<len(sequence_table):
        sequence=sequence_table[ex]
        chain.set(str(sequence))
        #ex += 1
    else:
        exit()
    return sequence



def next_line():
    global line
    line=next_sequence()
    lp=0
    steps_table=[]



step_by_step=Button(root,text="Krok po kroku",command=lambda:state_change(NFA_cal_step(line)))
run=Button(root,text="Automat",command=lambda:NFA_cal(line))
next=Button(root,text=">>>", command=lambda:next_line())
step_by_step.pack()
run.pack()
next.pack()


#guziki stanów mam już tablice obiektów
def state_disp():
    button_table=[]
    for i in range(0,12):
        button_table.append(Button(root,text="Q"+str(i),relief=RAISED))
        button_table[i].pack(side=LEFT)
    return button_table

buttons=state_disp()
root.mainloop()




#----------------------------------------------------------------------------------------------------------------------




