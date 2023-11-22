# Zadanie 4. Problem skoczka szachowego. Prosze napisac funkcje, która wypełnia pola szachownicy o
# wymiarach NxN ruchem skoczka szachowego.

from helpers import *

movements = [[1, 2], [2, 1], [1, -2], [2, -1], [-1, -2], [-2, -1], [-1, 2], [-2, 1]]


def knight_move(T, row, column, p):
    if T[row][column] != 0:
        listuj(T)
        return 0
    T[row][column] = p
    for v in movements:
        if 0 <= row + v[0] < len(T) and 0 <= column + v[1] < len(T):
            knight_move(T, row + v[0], column + v[1], p + 1)


n = 4
tab = [[0 for i in range(n)] for j in range(n)]

knight_move(tab, 3, 3, 1)
print(3 ** 27)
