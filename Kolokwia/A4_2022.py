import random

from listowanie import listuj

T = [[0 if random.random() < 0.85 else 1 for _ in range(8)] for _ in range(8)]
listuj(T)


def place(t):
    n, min_dist = len(t), len(t)
    middle = (n / 2, n / 2)
    max_new = 0
    best = None
    possible_checks = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for row in range(n):
        for col in range(n):
            dist = max(abs(middle[0] - row), abs(middle[1] - col))
            new = 0
            for p in possible_checks:
                next = row + p[0], col + p[1]
                if 0 <= next[0] < n and 0 <= next[1] < n:
                    if t[next[0]][next[1]] == 0:
                        new += 1
            if new > max_new:
                max_new = new
                best = row, col
            elif new == max_new and min_dist > dist:
                min_dist = dist
                best = row, col
    return best






print(place(T))
