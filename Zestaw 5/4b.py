# Zadanie 4. Problem skoczka szachowego. Prosze napisac funkcje, która wypełnia pola szachownicy o
# wymiarach NxN ruchem skoczka szachowego.

# Rozwiazanie z zajec z Garkiem

from helpers import list_table


def skok(T, w=0, k=0, ind=0):
    print(ind)
    N = len(T)
    T[w][k] = ind
    if ind == N * N:
        list_table(T)
    else:
        for i in range(8):
            if new_pos := mozliwy(T, w, k, i):
                skok(T, new_pos[0], new_pos[1], ind + 1)
    T[w][k] = 0


def mozliwy(T, w, k, ind):
    moves = [[1, 2], [2, 1], [1, -2], [2, -1], [-1, -2], [-2, -1], [-1, 2], [-2, 1]]
    next_col = k + moves[ind][1]
    next_row = w + moves[ind][0]
    if 0 <= next_row < len(T) and 0 <= next_col < len(T):
        if T[next_row][next_col] == 0:
            return next_row, next_col
    return False


n = 5
tab = [[0 for i in range(n)] for j in range(n)]
skok(tab, 3, 3)
