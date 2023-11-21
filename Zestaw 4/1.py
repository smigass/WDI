from listowanie import *


def spirala(N):
    t = [[0 for i in range(N)] for j in range(N)]
    v = (1, 0)
    x, y = 0, 0
    min_x, min_y = 0, 0
    max_x, max_y = N - 1, N - 1
    for i in range(N * N):
        t[y][x] = i + 1
        if x + v[0] > max_x:
            v = (0, 1)
            min_y += 1
        elif x + v[0] < min_x:
            v = (0, -1)
            max_y -= 1
        elif y + v[1] > max_y:
            v = (-1, 0)
            max_x -= 1
        elif y + v[1] < min_y:
            v = (1, 0)
            min_x += 1
        x, y = x + v[0], y + v[1]
    listuj(t)


spirala(4)
