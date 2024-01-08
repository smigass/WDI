import math

T = [False for i in range(16)]


def change_system(n, prev, new):
    if prev != 10:
        return change_system(change_system(n, prev, 10), 10, new)


def to_system(n, sys):
    if n > 0:
        to_system(n // sys, sys)
        if n % sys == 10:
            a = "A"
        elif n % sys == 11:
            a = "B"
        elif n % sys == 12:
            a = "C"
        elif n % sys == 13:
            a = "D"
        elif n % sys == 14:
            a = "E"
        elif n % sys == 15:
            a = "F"
        else: a = n % sys
        print(a, end="")
    # end if

def to_decimal(n, sys):
    l = int(math.log10(n)) + 1
    number = 0
    for i in range(l):
        last_digit = n % 10
        number += last_digit * (sys ** i)
        n //= 10
    return number

def to_binary(n):
    binary = 0
    i = 0
    while n != 0:
        binary += (n % 2) * 10**i
        i += 1
        n //= 2
    return binary

print(to_binary(48))



to_system(67478, 5)
