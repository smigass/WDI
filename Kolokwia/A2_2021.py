import math


def number_digits_set(n):
    t = [False for i in range(4)]
    for i in range(len(n)):
        t[n[i]] = True
    return t


def zgodne_4(a, b):
    a_digits = number_digits_set(quad_system(a))
    b_digits = number_digits_set(quad_system(b))
    for i in range(4):
        if b_digits[i] != a_digits[i]:
            return False
    return True


def quad_system(n):
    l = int(math.log(n, 4)) + 1
    t = [0 for i in range(l)]
    k = 1
    while n != 0:
        t[l - k] = n % 4
        n //= 4
        k += 1
    return t


def find_seq(T):
    max_seq = 1
    length = len(T)
    for i in range(length):
        curr_seq = 1
        for j in range(i + 1, length):
            if zgodne_4(T[i], T[j]):
                curr_seq += 1
        if curr_seq > max_seq:
            max_seq = curr_seq
    return max_seq


print(find_seq([13, 42, 23, 23, 33, 24, 33, 33, 18, 18, 23]))

def fib(n):
    a = 0
    b = 1
    for i in range(n - 1):
        a, b = b, b + a
    return a

print(fib(5))
