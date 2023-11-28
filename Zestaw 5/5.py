# Zadanie 5. Dany jest ciag zer i jedynek zapisany w tablicy T[N]. Prosze napisac funkcje, która odpowiada
# na pytanie czy jest mozliwe pociecie ciagu na kawałki z których kazdy reprezentuje liczbe pierwsza. Długosc
# kazdego z kawałków nie moze przekraczac 30. Na przykład dla ciagu 111011 jest to mozliwe, a dla ciagu
# 110100 nie jest mozliwe.
import math
import random

from helpers import is_prime, to_decimal


def add_next_binary(n, k):
    n *= 10
    return n + k


def check(T):
    print(T)
    if T[-2] == 0:
        return False
    return rec_search(T)


def is_decimal_prime(n):
    return is_prime(to_decimal(n, 2))


def rec_search(T, i=0, n=0, k=0):
    if k > 30:
        return False
    if i == len(T) - 1:
        if is_decimal_prime(n):
            return True
        else:
            return False
    # mozna (ale nie trzeba) wykonac ciecie w tym miejscu
    if is_decimal_prime(n) and T[i + 1] != 0:
        return rec_search(T, i + 1, 0, 0) or rec_search(T, i + 1, add_next_binary(n, T[i]), k + 1)
    # nie mozna wykonac ciecia wiec idzie dalej
    else:
        return rec_search(T, i + 1, add_next_binary(n, T[i]), k + 1)


length = 45
print(check([1, *[random.randint(0, 1) for i in range(length)], math.inf]))
