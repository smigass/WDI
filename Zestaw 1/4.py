number = int(input("Podaj liczbę do spierwiastkowania: "))


def isqrt(n):
    s = 0
    i = 1
    p = 0
    while s <= n:
        s += i
        i += 2
        p += 1

    return p - 1


print(isqrt(number))
