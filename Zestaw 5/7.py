# Zadanie 7. Dany jest zestaw odwazników T[N]. Napisac funkcje, która sprawdza czy jest mozliwe odwazenie
# okreslonej masy. Odwazniki mozna umieszczac tylko na jednej szalce.

from helpers import *


def waga(T, i, sum, curr_sum):
    if curr_sum == sum:
        return True
    if i == len(T):
        return False
    return waga(T, i + 1, sum, curr_sum) or waga(T, i + 1, sum, curr_sum + T[i])


tab = random_linear_list(15, 5)
print(tab)
print(waga(tab, 0, 20, tab[0]))
