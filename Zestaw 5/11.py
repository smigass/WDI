# Zadanie 11.
# Dana jest tablica T[N]. Prosze napisac program zliczajacy liczbe “enek” o okreslonym iloczynie.
from helpers import *


def enki(T, prod):
    result = 0

    def search(T, prod, index=0, cur_prod=1):
        nonlocal result
        if cur_prod * T[index] == prod:
            result += 1
        if index != len(T) - 1:
            search(T, prod, index + 1, cur_prod)
            search(T, prod, index + 1, cur_prod * T[index])

    search(T, prod)
    return result


Tab = random_linear_list(20, 15)
print(Tab)
print(enki(Tab, 36))
