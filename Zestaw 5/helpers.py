import math
import random


# funkcje pomocnicze do zadan

def list_table(T):
    print()
    for i in range(len(T)):
        for j in range(len(T)):
            print(T[i][j], end='\t')
        print('')
    print()


def random_list(n, a):
    return [[random.randint(1, a) for j in range(n)] for i in range(n)]


def random_linear_list(n, a):
    return [random.randint(1, a) for j in range(n)]


def random_float_list(n, a):
    return [random.randint(1, a) * random.random() * 2 for i in range(n)]


def random_float_tuple_list(n, a):
    return [(random.randint(1, a) * random.random() * 2, random.randint(1, a) * random.random() * 2) for i in range(n)]


def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n) + 1), 2):
        if n % i == 0:
            return False
    return True


def to_decimal(n, sys):
    if n == 0:
        return 0
    result = 0
    length = int(math.log(n, 10)) + 1
    for i in range(length):
        p = n % 10
        result += p * sys ** i
        n //= 10
    return result
