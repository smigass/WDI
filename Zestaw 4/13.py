import math

from listowanie import *

t = random_list(10, 4)

def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)+1), 2):
        if n % i == 0:
            return False
    return True

def complementary(a, b):
    return is_prime(a + b)

def exists_complementary(T, a, c):
    for i in range(len(T)):
        for j in range(len(T)):
            if j != c[1] or i != c[0]:
                if complementary(a, T[i][j]):
                    return True
    return False

def zerowanie(T):
    N = len(T)
    for i in range(N):
        for j in range(N):
            if not exists_complementary(T, T[i][j],(i, j)):
                T[i][j] = 0

listuj(t)
zerowanie(t)
listuj(t)