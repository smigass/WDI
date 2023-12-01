# Zadanie 19. Zadanie jak poprzednie. Funkcja sprawdzajaca czy król moze dostac sie z pola w,k do któregokolwiek
# z narozników.

# TODO - Zadanie do poprawy, jest oszukany append i sprawdzanie not in [].

import math

from helpers import random_list, list_table


def can_move(prev, new, history):
    if 0 <= new[0] <= 7 and 0 <= new[1] <= 7:
        p, n = board[prev[0]][prev[1]], board[new[0]][new[1]]
        last_prev = p % 10
        first_new = n // 10 ** (int(math.log10(n)))
        return last_prev < first_new and new not in history
    return False


min_dist = math.inf


def is_over(position):
    finals = [(0, 0), (0, 7), (7, 0), (7, 7)]
    for f in finals:
        if position == f:
            return True
    return False


def check(w, k, prev=None):
    print(w, k)
    if prev is None:
        prev = []
    if is_over((w, k)):
        return True
    moves = [(-1, 0), (-1, 1), (0, 1), (1, 0), (1, 1), (1, 0), (1, - 1), (0, - 1), (-1, -1)]
    for move in moves:
        next_move = (w + move[0], k + move[1])
        if can_move((w, k), next_move, prev):
            if check(next_move[0], next_move[1], [*prev, (w, k)]):
                print([*prev, (w, k)])
                return True
    return False


board = random_list(8, 50)
list_table(board)
print(check(4, 4))
