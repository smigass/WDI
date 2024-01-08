# Zadanie 20. Dana jest tablica T[N] [N] (reprezentujaca szachownice) wypełniona liczbami naturalnymi.
# Proszę napisac funkcje, która ustawia na szachownicy dwie wieze, tak aby suma liczb na „szachowanych”
# przez wieze polach była najwieksza. Do funkcji nalezy przekazac tablice, funkcja powinna zwrócic połozenie
# wiez. Uwaga- zakładamy, ze wieza szachuje cały wiersz i kolumne z wyłaczeniem pola na którym stoi
import random

from listowanie import list_table


def find_spot(board):
    N = len(board)
    cols = get_cols(board)
    best = (0, 0, 0)
    list_table(board)
    for i in range(N):
        for j in range(N):
            row_sum = sum(board[i]) - board[i][j]
            col_sum = sum(cols[j]) - board[i][j]
            if row_sum + col_sum > best[0]:
                best = (row_sum + col_sum, i, j)
    return best


def find_spots(board):
    a = find_spot(board)
    new_board = [[0 if a[2] == i or a[1] == j else board[j][i] for i in range(len(board))] for j in range(len(board))]
    b = find_spot(new_board)
    print([(a[1], a[2]), (b[1], b[2]), a[0], b[0], a[0] + b[0]])


def get_cols(board):
    cols = [[0 for _ in range(len(board))] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            cols[j][i] = board[i][j]
    return cols


def brut(board):
    cols = get_cols(board)
    N = len(board)
    best = [(0, 0), (0, 0), 0, 0, 0]
    for i in range(N):
        for j in range(N):
            sums1 = (sum(board[i]) - board[i][j], sum(cols[j]) - board[i][j])
            new_board = [[0 if i == b or a == j else board[b][a] for a in range(len(board))] for b in
                         range(len(board))]
            for r in range(N):
                for c in range(N):
                    if r != i or c != j and r >= i:
                        col = get_cols(new_board)[c]
                        sums2 = (sum(new_board[r]) - new_board[r][c], sum(col) - new_board[r][c])
                        if sum(sums1) + sum(sums2) > best[-1]:
                            best = [(i, j), (r, c), sum(sums1), sum(sums2), sum(sums1) + sum(sums2)]
                            #list_table(new_board)
    return best


n = 30
t = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]
find_spots(t)
print(brut(t))
