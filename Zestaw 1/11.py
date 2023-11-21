import math
import time

start = time.time()


def suma_dzielnikow(number):
    sum = 0
    for i in range(1, math.isqrt(number) + 1):
        if number % i == 0:
            sum += i
            if number % (number / i) == 0 and number / i != i and number / i != number:
                sum += number // i
    return sum


found = []
for i in range(3, 1000000):
    if i not in found:
        sum_i = suma_dzielnikow(i)
    sum_ii = suma_dzielnikow(sum_i)
    if i == sum_ii and sum_i != sum_ii:
        found.append(sum_ii)
        found.append(sum_i)
        print(i, sum_i)
end = time.time()

print((end - start) * 10 ** 3, 'ms')
