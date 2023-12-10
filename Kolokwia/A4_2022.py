import random

from listowanie import listuj

knight = "●"
empty = "○"
checked = "x"

N = 9
T = [[empty if random.random() < 0.95 else knight for _ in range(N)] for _ in range(N)]
listuj(T)

def check_checks(T):
    possible_checks = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(len(T)):
        for j in range(len(T)):
            if T[i][j] == knight:
                for p in possible_checks:
                    virtual_move = i + p[0], j + p[1]
                    if 0 <= virtual_move[0] < len(T) and 0 <= virtual_move[1] < len(T):
                        if T[virtual_move[0]][virtual_move[1]] != knight:
                            T[virtual_move[0]][virtual_move[1]] = checked
    return T


def place(t):
    t = check_checks(t)
    listuj(t)
    n, min_dist = len(t), len(t)
    middle = (n / 2, n / 2)
    max_new = 0
    best = None
    possible_checks = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for row in range(n):
        for col in range(n):
            if t[row][col] == knight: continue
            dist = max(abs(middle[0] - row), abs(middle[1] - col))
            new = 0
            for p in possible_checks:
                virtual_move = row + p[0], col + p[1]
                if 0 <= virtual_move[0] < n and 0 <= virtual_move[1] < n:
                    if t[virtual_move[0]][virtual_move[1]] == empty:
                        new += 1
            if new > max_new:
                max_new = new
                best = row, col
            elif new == max_new and min_dist > dist:
                min_dist = dist
                best = row, col
    return best


print(place(T))
