# Zadanie 6. Dana jest tablica T[N]. Prosze napisac funkcje, która znajdzie niepusty, najmniejszy (w sensie
# liczebnosci) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów tych elementów.
# Do funkcji nalezy przekazac tablice, funkcja powinna zwrócic sume elementów znalezionego podzbioru.
# Na przykład dla tablicy: [ 1,7,3,5,11,2 ] rozwiazaniem jest liczba 10.

from helpers import *


def recursive_search(T, i=0, length=0, el_sum=0, ids_sum=0):
    if el_sum == ids_sum and ids_sum != 0:
        return el_sum, length
    if i == len(T):
        return 0, math.inf

    s, best_l = recursive_search(T, i + 1, length + 1, el_sum + T[i], ids_sum + i)
    s1, best_l1 = recursive_search(T, i + 1, length, el_sum, ids_sum)

    better = (s, best_l) if best_l < best_l1 else (s1, best_l1)

    if i == 0:
        return better[0]
    else:
        return better


t1 = [1, 7, 3, 5, 11, 2]
# t = random_linear_list(10, 6)
print(recursive_search(t1))
