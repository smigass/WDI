import math

eps = 10 ** (-10)
a = 2020
x = 10
last = 0
while abs(x - last) > eps:
    x, last = x - ((math.pow(x, x) - a) / (math.pow(x, x) * (math.log(x, math.e) + 1))), x

print(x)
