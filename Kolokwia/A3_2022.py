import math
import random

from listowanie import listuj


def king(N, L):
    max_moves = 0
    T = [[0 for i in range(N)] for j in range(N)]
    for v in L:
        T[v[0]][v[1]] = math.inf
    listuj(T)

    def move_king(N, T, king_pos=(0, 0), p=1):
        nonlocal max_moves
        T[king_pos[0]][king_pos[1]] = p
        if king_pos[0] == N - 1 and king_pos[1] == N - 1:
            max_moves = p - 1 if p > max_moves else max_moves
        pos = [(0, 1), (1, 0), (-1, 0)]
        for k in pos:
            move = (king_pos[0] + k[0], king_pos[1] + k[1])
            if can_move(T, move):
                move_king(N, T, move, p + 1)
        T[king_pos[0]][king_pos[1]] = 0

    move_king(N, T)
    return max_moves if max_moves > 0 else None


def can_move(T, move):
    N = len(T)
    if 0 <= move[0] < N and 0 <= move[1] < N:
        return T[move[0]][move[1]] == 0
    return False


# funkcja uzytkowa do testowania
def r(m, M):
    return random.randint(m, M)


n = 7
# l = [(0, 3), (1, 2), (2, 1), (3, 0)]
t = [(r(0, n - 1), r(0, n - 1)) for _ in range(r(1, n ** 2 - 5))]

print(king(n, t))
