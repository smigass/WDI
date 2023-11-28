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

    def check(n1, n2, k=0):
        nonlocal counter
        if is_prime(k):
            counter += 1
        if n1 != 0:
            check(remove_first_digit(n1), n2, 10 * k + get_first_digit(n1))
        if n2 != 0:
            check(n1, remove_first_digit(n2), 10 * k + get_first_digit(n2))

    check(a, b)
    return counter


print(merge_numbers(123, 75))
