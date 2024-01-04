# Zadanie 24. Tablica T = [(x1, y1), (x1, y1), ...] zawiera połozenia N punktów o współrzednych opisanych
# wartosciami typu float. Proszę napisac funkcje, która zwróci najmniejsza odległosc miedzy srodkami ciezkosci
# 2 niepustych podzbiorów tego zbioru.
import math
import random

# DZIALA TYlKO PRZY N ≤ 9
sets = []


def srodek_c(T):
    x, y = 0, 0
    for v in T:
        x, y = x + v[0], y + v[1]
    return x / len(T), y / len(T)


def get_dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def get_sets(T: list, i: int = 0, s: list = []):
    global sets
    if i == len(T):
        if len(s) != 0:
            sc = srodek_c(s)
            sets += [s + [sc]]
        return s
    else:
        s1 = get_sets(T, i + 1, s)
        s2 = get_sets(T, i + 1, s + [T[i]])


def find_closest(s: list):
    minim = math.inf

    def find(sl: list, i: int = 0, u=None):
        if u is None:
            u = []
        nonlocal minim
        if len(u) == 2:
            dist = get_dist(u[0][-1], u[1][-1])
            if dist < minim:
                minim = dist
            return
        if i == len(sl):
            return
        find(sl, i + 1, u)
        find(sl, i + 1, u + [sl[i]])

    find(s)
    return minim


t = [(random.uniform(1, 10000), random.uniform(1, 10000)) for i in range(4)]
get_sets(t)
print(sets)
print(find_closest(sets))
