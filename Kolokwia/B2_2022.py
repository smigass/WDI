from listowanie import *

t = random_list(10, 50)


def rozklad(n):
    cnt = 0
    while n != 1:
        for i in range(2, n):
            pom = False
            while n % i == 0:
                pom = True
                n //= i
            if pom:
                cnt += 1
    return cnt == 2


def square(T):
    n = len(T)
    for i in range(2, n):
        for row in range(n - i):
            for col in range(n - i):
                iloraz = T[row][col] * T[row + i][col] * T[row][col + i] * T[row + i][col + i]
                if rozklad(iloraz):
                    return i
    return 0


print(square(t))
