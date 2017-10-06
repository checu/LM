import tkinter
from tkinter import *
from tkinter import messagebox


tablica_stanow = [[1, 2, 5], [2, 3, 6], [3, 4, 7], [4, 5, 0], [5, 6, 0], [6, 7, 0], [7, 0, 0], [0, 0, 0]]
nominaly = [1, 2, 5]
suma = 0

# rozmiar tablica_stanow[7][2]
def zwroc_stan(suma, nominal):
    i_no = suma + nominal  # nowa kwota w parkomacie

    if nominal == 1:
        suma = tablica_stanow[i_no - 1][0]
        print(suma, 1)
    elif nominal == 2:
        suma = tablica_stanow[i_no - 2][1]
        print(suma, 2)
    elif nominal == 5:
        suma = tablica_stanow[i_no - 5][2]
        print(suma, 5)

    if suma == 0:
        print("Zwrot monet")

    print ("Saldo wynosi", suma, "zl")
    return suma


top =tkinter.Tk()
var2=StringVar()
label=Label(top,textvariable=var2)

def guzik(nominal):
    global suma
    suma= zwroc_stan(suma, nominal)
    var2.set(str(suma)+" zl")
    if suma==7:
        messagebox.showinfo("INFO","Pobierz bilet")
    elif suma==0:
        messagebox.showinfo("UWAGA","Zwrot monet")
    else:
        pass



button_1zl=tkinter.Button(top,text="1zl",command=lambda: guzik(1),bg="#CC3300",fg="white")
button_1zl.pack(padx=5, pady=10,side=LEFT)
button_2zl=tkinter.Button(top,text="2zl",command=lambda:guzik(2),bg="#CC6600",fg="white")
button_2zl.pack(padx=5, pady=20,side=LEFT)
button_5zl=tkinter.Button(top,text="5zl",command=lambda: guzik(5),bg="#CC9900",fg="white")
button_5zl.pack(padx=5, pady=20,side=LEFT)



var =StringVar()

title=Label(top,textvariable=var)



var.set ("PARKOMAT")

var2.set("0 zl")

title.pack()
button_1zl.pack()
button_2zl.pack()
button_5zl.pack()
label.pack()

top.mainloop()