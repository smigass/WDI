# Zadanie 17. Dane sa dwie liczby naturalne z których budujemy trzecia liczbe. W budowanej liczbie musza
# wystapic wszystkie cyfry wystepujace w liczbach wejsciowych. Wzajemna kolejnosc cyfr kazdej z liczb
# wejsciowych musi byc zachowana. Na przykład majac liczby 123 i 75 mozemy zbudowac liczby 12375, 17523,
# 75123, 17253, itd. Prosze napisac funkcje która wyznaczy ile liczb pierwszych mozna zbudowac z dwóch
# zadanych liczb.

import math

from helpers import is_prime


def get_first_digit(n):
    length = int(math.log(n, 10) + 1)
    return n // 10 ** (length - 1)


def remove_first_digit(n):
    length = int(math.log(n, 10) + 1)
    return n - get_first_digit(n) * 10 ** (length - 1)


def merge_numbers(a, b):
    counter = 0

    def check(n1, n2, curr_n=0):
        nonlocal counter
        if is_prime(curr_n):
            counter += 1
        if n1 != 0:
            check(remove_first_digit(n1), n2, 10 * curr_n + get_first_digit(n1))
        if n2 != 0:
            check(n1, remove_first_digit(n2), 10 * curr_n + get_first_digit(n2))

    check(a, b)
    return counter


print(merge_numbers(123, 75))
