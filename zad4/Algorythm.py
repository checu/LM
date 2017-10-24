# ODN

#expression=input("Podaj wyrażenie?")

#charters=list(expression.split())
charters=""

calc_sign=["+","-","^","*","/"]

def ODN(calculation,indeks):
    global charters
   # kogut=charters
    if calculation=="+":
        k=int(charters[indeks-2])+int(charters[indeks-1])
        charters.insert(indeks,int(charters[indeks-2])+int(charters[indeks-1]))
        charters.pop(indeks - 1)
        charters.pop(indeks - 2)
        # charters.remove(charters[indeks-1])
        # charters.remove(charters[indeks-2])
    elif calculation=="-":
        charters.insert(indeks,int(charters[indeks-2])-int(charters[indeks-1]))
        # z=charters[indeks - 1]
        # x=charters[indeks - 2]
        w=charters.pop(indeks-1)
        y=charters.pop(indeks-2)
        # charters.remove(charters[indeks - 1])
        # charters.remove(charters[indeks - 2])
    elif calculation == "^":
        charters.insert(indeks,int(charters[indeks-2])**int(charters[indeks-1]))
        charters.pop(indeks - 1)
        charters.pop(indeks - 2)
        # charters.remove(charters[indeks - 1])
        # charters.remove(charters[indeks - 2])
    elif calculation == "*":
        charters.insert(indeks,int(charters[indeks-2])*int(charters[indeks-1]))
        charters.pop(indeks - 1)
        charters.pop(indeks - 2)
        # charters.remove(charters[indeks - 1])
        # charters.remove(charters[indeks-2])
    elif calculation == "/":
        charters.insert(indeks,int(charters[indeks-2])/int(charters[indeks-1]))
        charters.pop(indeks - 1)
        charters.pop(indeks - 2)
        # charters.remove(charters[indeks - 1])
        # charters.remove(charters[indeks - 2])

    return charters


def ODNN(eque):
    global charters
    charters=eque
    print(charters)
    for charter in charters:
        for sign in calc_sign:
            if charter ==sign:
                indeks=charters.index(charter)
                ODN(charter,indeks)
                charters.remove(charter)
                if len(charters) > 1:
                    ODNN(charters)
    return charters
       # kucyk=charters
#ODNN()
#print (charters)




