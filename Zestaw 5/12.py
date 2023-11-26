# Zadanie 11.
# Dana jest tablica T[N]. Prosze napisac program zliczajacy liczbe “enek” o okreslonym iloczynie.
from helpers import *


def enki(T, prod, index=0, cur_prod=1, elements=[]):
    if cur_prod * T[index] == prod:
        print(elements+[T[index]])
    if index != len(T) - 1:
        enki(T, prod, index + 1, cur_prod, elements)
        enki(T, prod, index + 1, cur_prod * T[index], elements + [T[index]])


Tab = random_linear_list(10, 15)
print(Tab)
print(enki(Tab, 36))
