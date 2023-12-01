# Zadanie 19. Zadanie jak poprzednie. Funkcja sprawdzajaca czy król moze dostac sie z pola w,k do któregokolwiek
# z narozników.

import math

from helpers import random_list, list_table


def can_move(prev, new, history):
    if 0 <= new[0] <= 7 and 0 <= new[1] <= 7:
        if distance[prev[0]][prev[1]] >= distance[new[0]][new[1]]:
            p, n = board[prev[0]][prev[1]], board[new[0]][new[1]]
            last_prev = p % 10
            first_new = n // 10 ** (int(math.log10(n)))
            return last_prev < first_new and new not in history
    return False


min_dist = math.inf


def check(w, k, prev=[]):
    dist = distance[w][k]
    global min_dist
    if dist < min_dist:
        min_dist = dist
    if dist == 0:
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
distance = [[max(abs(i - 7), abs(j - 7)) for j in range(8)] for i in range(8)]
list_table(board)
print(check(5, 5))
