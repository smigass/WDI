# Zadanie 32. Dana jest tablica T[N] zawierajaca liczby naturalne. Prosze napisac funkcje, która odpowiada
# na pytanie, czy sposród (niekoniecznie wszystkich) elementów tablicy mozna utworzyc dwa podzbiory o
# jednakowej sumie elementów, tak aby suma mocy obu podzbiorów wynosiła k. Do funkcji nalezy przekazac
# wyłacznie tablice T oraz liczbe naturalna k, funkcja powinna zwrócic wartosc typu bool.
from helpers import *


def zad32(T, k):
    return check(T, k)


def check(T, k, index=0, set1=[], set2=[]):
    if len(set1) + len(set2) > k:
        return False
    if sum(set2) == sum(set1) and set1 != set2:
        if len(set1) + len(set2) == k:
            print(set1, set2)
            return True
    if index < len(T):
        return ((check(T, k, index + 1, set1, set2) or
                check(T, k, index + 1, set1 + [T[index]], set2) or
                check(T, k, index + 1, set1, set2 + [T[index]]))
                # zakomentowanie linii ponieżej policzy tylko rozlaczne podzbiory
                or check(T, k, index + 1, set1 + [T[index]], set2 + [T[index]]))
    return False


t = random_linear_list(15, 2000)
print(zad32(t, 10))
