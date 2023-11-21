import math
import random

from helpers import is_prime


def check(T):
    print(T)
    if T[-1] == 0:
        return False
    for i in range(len(T) - 1):
        start_frag = [1 for _ in range(i + 2)]
        check_fragment(T, start_frag)


def check_fragment(T, fragment):
    if sum(fragment) == len(T):
        check_primes(T, fragment)
        return 0
    fragment[0] += 1
    check_fragment(T, fragment)
    k = 0
    for i in range(1, len(fragment)):
        if fragment[i] < 30:
            fragment[i] += 1
            fragment[i - 1 - k] -= 1
            k = 0
        else:
            k += 1
        check_fragment(T, fragment)


def check_primes(T, fragment):
    index = 0
    for v in fragment:
        if not is_prime(join_numbers(T[index:v + index])):
            return False
        index += v
    print(True)


def join_numbers(T):
    s = 0
    for i in range(-1, -len(T) - 1, -1):
        s += T[i] * 10 ** (abs(i) - 1)
    return s


t = [1] + [math.floor(random.random() * 2) for _ in range(random.randint(3, 20))]

print(check([1, 1, 0, 0, 1, 1]))
