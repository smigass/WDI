import math
import random
from listowanie import listuj

def tylko_nieparzyste(number):
    for i in range(int(math.log10(number)) + 1):
        if (number % 10) % 2 == 0:
            return False
        number //= 10
    return True

def test(N):
    t = [[random.randrange(1, 1000, 2) for i in range(N)] for j in range(N)]
    listuj(t)
    for i in range(N):
        found = False
        j = 0
        while not found:
            if tylko_nieparzyste(t[i][j]):
                found = True
            if j + 1 == N:
                return False
            j += 1
    return True

print(test(10))

