# Zadanie 1. Prosze napisac funkcje, która jako argument przyjmuje liczbe całkowita i wypisuje wszystkie
# co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreslenie z liczby pierwotnej co najmniej jednej
# cyfry.


import math


def wykresl(number, t):
    length = int(math.log10(number)) + 1
    if length < 2:
        return 0
    if is_prime(number):
        if number not in t:
            print(number)
            t.append(number)
    for i in range(length):
        cp = number
        k = 0
        next_number = 0
        for j in range(length):
            if i != j:
                last = cp % 10
                next_number += last * 10 ** k
                k += 1
            cp //= 10
        wykresl(next_number, t)


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


wykresl(47263, [])
