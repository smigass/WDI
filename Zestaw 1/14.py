import math

def maclaurin(x, precision):
    value = 1
    flag = -1
    power = 2
    for i in range(1, precision):
        value += flag*x**power*1/silnia(power)
        power+=2
        flag*=-1
    return value

def silnia(n): return n*silnia(n-1) if n > 1 else 1

print(maclaurin(3,200))