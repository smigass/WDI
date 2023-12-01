# Zadanie 22. Dana jest tablica T[N] zawierajaca liczby naturalne. Po tablicy mozemy przemieszczac się
# według nastepujacej zasady: z pola o indeksie i mozemy przeskoczyc na pole o indeksie i+k jezeli k jest
# czynnikiem pierwszym liczby t[i] mniejszym od t[i]. Proszę napisac funkcje, która zwraca informacje czy jest
# mozliwe przejscie z pola o indeksie 0 na pole o indeksie N-1. Funkcja powinna zwrócic liczbe wykonanych
# skoków lub wartosc -1 jezeli powyzsze przejscie nie jest mozliwe.

from helpers import random_linear_list, is_prime


def can_jump(val, k):
    if is_prime(k) and val % k == 0 and k < val:
        return True


# hist-zmienna pogladowa pokazujaca wynik rekurencji (skad -> o ile -> gdzie)
def jump(T, ind=0, jumps=0, hist=[]):
    N = len(T)
    if ind == N - 1:
        print(hist)
        return jumps
    for i in range(1, N - ind):
        if can_jump(T[ind], i):
            ans = jump(T, ind + i, jumps + 1, [*hist, (T[ind], i, T[ind + i])])
            if ans != -1:
                return ans
    return -1


n = 25
l = random_linear_list(n, 40)
print(l)
print(jump(l))
