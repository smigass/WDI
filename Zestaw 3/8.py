import random


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    for i in range(3, int(n ** 0.5 + 1), 2):
        if n % i == 0:
            return False
    return True


def is_possible(t):
    print(t)
    n = len(t) - 1
    k = 0
    if not is_prime(n):
        return False
    else:
        if t[k] % n == 0:
            return True
    return False

print(is_possible([random.randint(1, 100) for i in range(random.randint(1, 50))]))

