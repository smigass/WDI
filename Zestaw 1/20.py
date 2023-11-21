import math


first_a = int(input("Podaj pierwszy element ciągu A: "))
first_b = int(input("Podaj pierwszy element ciągu B: "))


def find_limit(fa, fb, eps):
    last_a = fa
    last_b = fb
    diff = abs(last_b - last_a)
    while diff > eps:
        last_a, last_b = math.sqrt(last_b * last_a), (last_a + last_b) / 2
        diff = abs(last_b - last_a)
    return last_a


print(find_limit(first_a, first_b, 10 ** (-15)))
