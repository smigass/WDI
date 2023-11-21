import math
import random
from listowanie import listuj


def singleton(T1, T2):
    n = len(T1)
    m = len(T2)
    listuj(T1)
    tab = [0 for _ in range(n)]
    k = 0
    flag = True
    mem = T1[znajdz_najmniejszy(T1, tab)][tab[znajdz_najmniejszy(T1, tab)]]
    for _ in range(m):
        w = znajdz_najmniejszy(T1, tab)
        x = T1[w][tab[w]]
        if tab[w] != n:
            tab[w] += 1
        if x == mem:
            flag = False
        elif x != mem and flag:
            flag = True
            T2[k] = mem
            k += 1
        else:
            flag = True
        mem = x
        if _ == m - 1:
            T2[k] = x

        #print(tab)
    return T2

def znajdz_najmniejszy(T, t):
    wiersz = 0
    for i in range(0, len(t)):
        if T[i][t[i]] < T[wiersz][t[wiersz]]:
            wiersz = i
    return wiersz




K = 5
T1 = [sorted([random.randint(1, 100) for i in range(K)]+[math.inf]) for j in range(K)]
T2 = [0 for _ in range(K * K)]
print(singleton(T1, T2))
