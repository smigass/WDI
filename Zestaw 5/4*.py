# Zadanie 4. Problem skoczka szachowego. Prosze napisac funkcje, która wypełnia pola szachownicy o
# wymiarach NxN ruchem skoczka szachowego.


from helpers import *


def knight_move(T, row, col, p=1):
    T[row][col] = p
    moves = [[1, 2], [2, 1], [1, -2], [2, -1], [-1, -2], [-2, -1], [-1, 2], [-2, 1]]
    if p == len(T) ** 2:
        return True
    for v in moves:
        next_row = row + v[0]
        next_col = col + v[1]
        if 0 <= next_row < len(T) and 0 <= next_col < len(T):
            if T[next_row][next_col] == 0:
                if knight_move(T, row + v[0], col + v[1], p + 1):
                    return True
    T[row][col] = 0
    return False


n = 7
tab = [[0 for i in range(n)] for j in range(n)]
knight_move(tab, 6, 6)
list_table(tab)
