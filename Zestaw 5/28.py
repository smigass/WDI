# Zadanie 28. Dany jest zbiór N liczb naturalnych umieszczony w tablicy T[N]. Prosze napisac funkcje,
# która zwraca informacje, czy jest mozliwy podział zbioru N liczb na trzy podzbiory, tak aby w kazdym
# podzbiorze, łaczna liczba jedynek uzyta do zapisu elementów tego podzbioru w systemie dwójkowym była
# jednakowa. Na przykład: [2, 3, 5, 7, 15] ! true, bo podzbiory f2,7g f3,5g f15g wymagaja uzycia 4 jedynek,
# [5, 7, 15] ! false, podział nie istnieje.

from helpers import *


def binary_ones(number):
    counter = 0
    while number > 0:
        counter += number % 2
        number //= 2
    return counter


def ones_in_set(set_):
    s = 0
    for num in set_:
        s += binary_ones(num)
    return s


def check_sets(sets):
    return ones_in_set(sets[0]) == ones_in_set(sets[1]) == ones_in_set(sets[2])


def split(T, index=0, set1=[], set2=[], set3=[]):
    N = len(T)
    if index == N:
        return check_sets([set1, set2, set3])
    return (split(T, index + 1, set1 + [T[index]], set2, set3)
            or split(T, index + 1, set1, set2 + [T[index]],set3)
            or split(T, index + 1, set1, set2,set3 + [T[index]]))


t = random_linear_list(15, 20)
print(split([5, 7, 15]))
