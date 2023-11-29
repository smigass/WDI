# Zadanie 18. W szachownicy o wymiarach 8x8 kazdemu z pól przypisano liczbe naturalna. Na ruchy króla
# nałozono dwa ograniczenia: król moze przesunac sie na jedno z 8 sasiednich pól jezeli ostatnia cyfra liczby na
# polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do obranego celu
# (np. naroznika) król nie moze wykonac ruchu, który powoduje oddalenie go od celu. Dana jest globalna tablica
# T[8][8] wypełniona liczbami naturalnymi reprezentujaca szachownice. Lewy górny naroznik ma współrzedne
# w=0 i k=0. Prosze napisac funkcje sprawdzajaca czy król moze dostac sie z pola w,k do prawego dolnego
# naroznika.

import math

from helpers import random_list, list_table


# TODO - make it go the other way (from the bottom-right corner to position (w, k))
def can_move(prev, new, history):
    if distance[prev[0]][prev[1]] >= distance[new[0]][new[1]]:
        p, n = board[prev[0]][prev[1]], board[new[0]][new[1]]
        last_prev = p % 10
        first_new = n // 10 ** (int(math.log10(n)))
        return last_prev < first_new and new not in history
    return False


min_dist = 100


def check(w, k, prev=None):
    if prev is None:
        prev = []
    dist = distance[w][k]
    global min_dist
    if dist < min_dist:
        min_dist = dist
    if dist == 0:
        return True
    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= w + i <= 7 and 0 <= k + j <= 7:
                if can_move((w, k), (w + i, k + j), prev):
                    if i != 0 or j != 0:
                        if check(w + i, k + j, [*prev, (w, k)]):
                            return True
    return False


board = random_list(8, 50)
distance = [[max(abs(i - 7), abs(j - 7)) for j in range(8)] for i in range(8)]
list_table(board)
print(check(5,7))
