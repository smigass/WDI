# Zadanie 21. Tablica T [8] [8] zawiera liczby naturalne. Proszę napisac funkcje, która sprawdza, czy mozna
# wybrac z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest, aby zadne dwa wybrane
# elementy nie lezały w tej samej kolumnie ani wierszu. Do funkcji nalezy przekazac wyłacznie tablice oraz
# wartosc sumy, funkcja powinna zwrócic wartosc typu bool.

from helpers import *


def zad21(T, s):
    return check_set(T, s)


def can_add(used, cords, nexts, s):
    if nexts > s:
        return False
    for u in used:
        if u[0] == cords[0] or u[1] == cords[1]:
            return False
    else:
        return True


def check_set(T, s, cur_s=0, cords=(0, 0), used=[]):
    N = len(T)
    if cords[1] == len(T):
        return check_set(T, s, cur_s, (cords[0] + 1, 0), used)
    if cords[0] == len(T):
        return False
    next_sum = T[cords[0]][cords[1]] + cur_s
    if can_add(used, cords, next_sum, s) and next_sum == s and len(used) > 0:
        print([*used, cords])
        return True
    if can_add(used, cords, next_sum, s):
        return (check_set(T, s, next_sum, (cords[0], cords[1] + 1), [*used, cords]) or
                check_set(T, s, cur_s, (cords[0], cords[1] + 1), used))
    else:
        return check_set(T, s, cur_s, (cords[0], cords[1] + 1), used)


l = random_list(8, 81)
list_table(l)
print(zad21(l, 81))
