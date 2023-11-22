# Zadanie 10. Rekurencyjne obliczanie wyznacznika z macierzy (tresc oczywista)

from helpers import *


def det_2x2(T):
    return T[0][0] * T[1][1] - T[0][1] * T[1][0]


def det_nxn(T):
    length = len(T)
    s = 0
    if length == 2:
        return det_2x2(T)
    for i in range(length):
        s += ((-1) ** i) * T[i][0] * det_nxn(cut_tab(T, i))
    return s


def cut_tab(T, row):
    new_tab, k = [[0 for _ in range(len(T) - 1)] for p in range(len(T) - 1)], 0
    for i in range(len(T)):
        if i != row:
            for j in range(1, len(T)):
                new_tab[k][j - 1] = T[i][j]
            k += 1
    return new_tab


matrix = random_list(random.randint(3, 10), 4)
listuj(matrix)

print(det_nxn(matrix))
