import math


def sequence(n):
    if n == 0:
        return math.sqrt(0.5)
    return math.sqrt(0.5 + 0.5 * sequence(n - 1))


not_pi = 1
precision = 300
for i in range(precision):
    not_pi *= sequence(i)

pi = 2 / not_pi
print(pi)
