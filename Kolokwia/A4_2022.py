import random

from listowanie import listuj

knight = "●"
empty = "○"
checked = "x"

N = 9
T = [[empty if random.random() < 0.90 else knight for _ in range(N)] for _ in range(N)]
listuj(T)


# Funkcja find_checks zaznacza w tablicy poczatkowej pola zaszachowane przez
# poczatkowe ustawienie skoczkow (zaznacza puste pole "○" ktore sa szachowane na "x")
def find_checks(tab):
    possible_checks = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(len(tab)):
        for j in range(len(tab)):
            if tab[i][j] == knight:
                for p in possible_checks:
                    virtual_move = i + p[0], j + p[1]
                    if 0 <= virtual_move[0] < len(tab) and 0 <= virtual_move[1] < len(tab):
                        if tab[virtual_move[0]][virtual_move[1]] != knight:
                            tab[virtual_move[0]][virtual_move[1]] = checked
    return tab


def place(t):
    t = find_checks(t)
    listuj(t)
    n, min_dist = len(t), len(t)
    middle = (n / 2, n / 2)
    max_new = 0
    best = None
    possible_checks = [(1, 2), (2, 1), (1, -2), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for row in range(n):
        for col in range(n):
            if t[row][col] == knight:
                continue
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
