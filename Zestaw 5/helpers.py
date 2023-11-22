import math
import random


def listuj(T):
    for i in range(len(T)):
        print(T[i])
    print()


def random_list(n, a):
    return [[random.randint(1, a) for j in range(n)] for i in range(n)]


def random_linear_list(n, a):
    return [random.randint(1, a) for j in range(n)]


def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n) + 1), 2):
        if n % i == 0:
            return False
    return True
