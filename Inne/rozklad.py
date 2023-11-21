import math


def rozklad(n):
    i = 2
    while n >= 2:
        while n % i == 0:
            print(i)
            n //= i
        i += 1

def silnia(n):
    s = 1
    for i in range(1,n + 1):
        s *= i
    return s

def rozklad(n):
    d = []
    while n != 1:
        for i in range(2,n):
            while n % i == 0:
                d += [i]
                n //= i
    return d

def dzielniki(n):
    d = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            d += [i]
            if n % (n//i) == 0 and i != n // i:
                d += [n // i]

    return sorted([1]+d+[n])
c = 0
for v in dzielniki(silnia(10)):
    if v % 20 == 0 or v % 24 == 0 or v % 32 == 0:
        c += 1




print(silnia(7) - 8 * silnia(6) + 48 * silnia(4))
