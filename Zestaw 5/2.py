# Zadanie 2. ”Waga” liczby jest okreslona jako ilosc róznych czynników pierwszych liczby. Na przykład
# waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierajaca liczby
# naturalne. Prosze napisac funkcje, która sprawdza czy mozna elementy tablicy podzielic na 3 podzbiory o
# równych wagach. Do funkcji nalezy przekazac wyłacznie tablice, funkcja powinna zwrócic wartosc typu Bool.


def waga(n):
    w = 0
    if n == 1:
        return 0
    while n != 1:
        for i in range(2, n + 1):
            f = False
            while n % i == 0:
                if not f:
                    f = True
                    w += 1
                n //= i
    return w


def zad2(t):
    wagi = [waga(t[i]) for i in range(len(t))]
    print(wagi)
    if sum(wagi) % 3 != 0:
        return False
    return check(wagi, 0, 0, 0)


def check(t, a, b, c, n=0):
    if n == len(t):
        return a == b == c
    return check(t, a + t[n], b, c, n + 1) or check(t, a, b + t[n], c, n + 1) or check(t, a, b, c + t[n], n + 1)


print(zad2([1, 72, 322, 5, 115, 2]))
