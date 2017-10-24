from GUINEF import *

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
        index += 1
        if index == 1:
            state = state_table[0][int(element)]

            steps_table.append(state)

        else:
            state = NFA(element, max(steps_table[index-2]))

            steps_table.append(state)

    return steps_table


print(NFA_cal("124456"))
# print (NFA("3"))
