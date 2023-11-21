import math


def nwd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


def nww(a, b):
    ca = a
    cb = b
    while ca != cb:
        if ca > cb:
            cb += b
        else:
            ca += a
    return ca


def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def rozklad(n, ile):
    if is_prime(n):
        return [n]
    if not ile:
        t = [0 for i in range(rozklad(n, True))]
    s = 0
    k = 0
    i = 2
    while n != 1:
        while n % i == 0:
            if ile:
                s += 1
            else:
                t[k] = i
                k += 1
            n //= i
        i += 1
    return s if ile else t

def dzielniki(n, ile):
    s = 0
    if not ile:
        t = [0 for i in range(dzielniki(n, True) + 2)]
        t[0] = 1
        t[len(t) - 1] = n
    k = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if not ile:
                t[k] = i
            if n // i != i:
                if not ile:
                    t[len(t) - 1 - k] = n // i
                s += 1
            k += 1
            s += 1
    return s if ile else t


a = 1
b = 36
print(f"rozkład {a}: {rozklad(a, False)}")
print(f"pierwsza {a}: {is_prime(a)}")
print(f"nww({a}, {b}): {nww(a, b)}")
print(f"nwd({a}, {b}): {nwd(a, b)}")
print(f"dzielniki: {a}: {dzielniki(a, False)}")
print([8,9,0,8,9,0])