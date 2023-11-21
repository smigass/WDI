import math
import random

from listowanie import *


def znajdz_index(T1, t):
    index = 0
    for i in range(0, len(t)):
        if T1[i][t[i]] < T1[index][t[index]]:
            index = i
    return index


def przepisywanie(T1, T2):
    m = len(T2)
    n = len(T1)
    for i in range(n):
        T1[i] = T1[i]+[math.inf]
    t = [0 for _ in range(n)]
    listuj(T1)
    for i in range(m):
        x = znajdz_index(T1, t)
        T2[i] = T1[x][t[x]]
        t[x] += 1
    return T2


k = 4
T1 = [sorted([random.randint(1, 100) for a in range(k)]) for b in range(k)]
T2 = [0 for a in range(k * k)]

print(przepisywanie(T1, T2))
