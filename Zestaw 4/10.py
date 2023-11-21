from listowanie import *


def zerowa_tablica(T):
    n = len(T)
    listuj(T)
    kolumny = [False for i in range(n)]
    for i in range(n):
        zero_w_wierszu = False
        for j in range(n):
            if T[i][j] == 0:
                zero_w_wierszu = True
                kolumny[j] = True
        if not zero_w_wierszu:
            return False
    for v in kolumny:
        if not v:
            return False
    return True


tab = [
    [0, 1, 2, 3],
    [0, 1, 2, 3],
    [0, 2, 1, 3],
    [0, 0, 0, 0]
]

print(zerowa_tablica(tab))
