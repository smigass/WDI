# Zadanie 8. Poprzednie zadanie, ale odwazniki mozna umieszczac na obu szalkach.

from helpers import *


def waga(T, i, sum, side1=0, side2=0):
    if abs(side1 - side2) == sum:
        return True
    if i == len(T):
        return False
    return waga(T, i + 1, sum, side1 + T[i], side2) or waga(T, i + 1, sum, side1, side2 + T[i]) or waga(T, i + 1, sum,
                                                                                                        side1, side2)


tab = random_linear_list(15, 5)

print(tab)
print(waga(tab, 0, 20))
