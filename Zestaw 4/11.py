import math

from listowanie import *


def find_set(n, default):
    t = [False for i in range(10)]
    if n == -1:
        return default
    l = int(math.log10(n) + 1)
    for i in range(l):
        last_digit = n % 10
        t[last_digit] = True
        n //= 10
    return t

def convert_tab(T):
    n = len(T)
    t = [[-1] + T[i - 1] + [-1] if i > 0 and i < n + 1 else [-1 for j in range(n + 2)] for i in range(n + 2)]
    return t

def neighbours(T):
    n = len(T)
    res = 0
    restab = []
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            element = T[i][j]
            s = find_set(element, False)
            upper = find_set(T[i - 1][j], s)
            bottom = find_set(T[i + 1][j], s)
            right = find_set(T[i][j + 1], s)
            left = find_set(T[i][j - 1], s)
            if upper == s and bottom == s and right == s and left == s:
                res += 1
                restab.append((i - 1 ,j - 1))
    return res, restab

tab = random_list(5, 2)
listuj(tab)
print(neighbours(convert_tab(tab)))