# analizator skladniowy --- o co chodzi


# wczytywanie ciagow z pliku


operator="+-*/^"
zero="0"
cyfra="0123456789"
cyfra1="123456789"
wyrazenie=""

index=0



def index_incr():
    global index
    global wyrazenie
    if  index+1<len(wyrazenie):
        index+=1
        return True
    else:#koniec wyrazenia
        return False

def minus():
    global wyrazenie
    if wyrazenie[0] == "-":
        return True
        # if index_incr():
        #     return True
        # else:
        #     return False
    else:
        return False

# def zero():
#     global wyrazenie
#     global index
#     if wyrazenie[index] =="0":
#         return True
#     else:
#         return False

def operator():
    global wyrazenie
    global index
    if  wyrazenie[index] in ["+","-","/","*","^"]:
        return True
    else:
        return False


def liczba():
    global wyrazenie
    global cyfra1
    global cyfra
    global index
    index_h=index
    if wyrazenie[index].isdigit():
        while wyrazenie[index].isnumeric():
            if index_h==index:
                if wyrazenie[index] in zero:
                    if not index_incr():
                        break
                    return True
                elif wyrazenie[index] not in cyfra1:
                    return False
            else:
                if wyrazenie[index] not in cyfra:
                    return False
            if not index_incr():
                break
        return True
    else:
        return False

i=0

def operator_liczba():
    global index
    global wyrazenie
    global i
    if operator():
        i=+1
        if index_incr():
            # print("incre", index)
            if liczba():
                # print("liczba",index)
                # if index_incr():
                # index-=1
                return operator_liczba()
                # else:
                #     return True
            else:
                return False
        else:
            return False
    else:
        if wyrazenie[index] in cyfra and not index_incr() and i>0:
            return True
        else:
         return False

# print("operator_liczba",operator_liczba())


def S(expression):
    global index
    global wyrazenie
    wyrazenie=expression
    index=0
    if minus():
        if index_incr():
            if liczba():
                if operator_liczba():
                    return True
                else:
                    return False
        else:
            return False
    elif liczba():
        if operator_liczba():
            # print(operator_liczba())
            return True
        else:
            return False
    else:
        return False

# z=S()
# print("s",S("2+2"))
# print('co',wyrazenie)
# print("wyrazenie",z)











