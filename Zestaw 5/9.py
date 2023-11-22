# Zadanie 8. Poprzednie zadanie, ale odwazniki mozna umieszczac na obu szalkach.

from helpers import *


def add_element(T, el):
    return [T[i] if i < len(T) else el for i in range(len(T) + 1)]


def waga(T, i, suma, side1=[], side2=[]):
    if abs(sum(side1) - sum(side2)) == suma:
        return side1, side2
    if i == len(T):
        return False
    return waga(T, i + 1, suma, add_element(side1, T[i]), side2) or waga(T, i + 1, suma, side1, add_element(side2, T[i])) or waga(T, i + 1, suma,
                                                                                                          side1, side2)


tab = random_linear_list(10, 5)

print(tab)
print(waga(tab, 0, 2))
