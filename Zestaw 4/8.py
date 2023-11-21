import random

from listowanie import listuj


def znaleziono_ciag(T):
    listuj(T)
    n = len(T)
    for i in range(n - 2):
        t1 = [0 for _ in range(n - i)]
        for l in range(n - i):
            t1[l] = T[l + i][l]
        istnieje = istnieje_ciag(t1)
        if istnieje[0]:
            return istnieje
    for j in range(1, n - 2):
        t2 = [0 for _ in range(n - j)]
        for l in range(n - j):
            t2[l] = T[l][l + j]
        istnieje = istnieje_ciag(t2)
        if istnieje[0]:
            return istnieje
    return False


def istnieje_ciag(t):
    last_q = t[1] / t[0]
    max_counter = 1
    counter = 2
    for i in range(2, len(t)):
        if t[i] / t[i - 1] == last_q:
            counter += 1
            if counter > max_counter:
                max_counter = counter
        else:
            last_q = t[i] / t[i - 1]
            counter = 2
    if max_counter >= 3:
        print(t)
        return True, max_counter
    else:
        return False, max_counter


k = 6
t = [[random.randint(1, 1000) for a in range(k)] for b in range(k)]
li = [
    [1, 2, 3, 4, 5],
    [1, 2, 4, 3, 4],
    [2, 1, 1, 8, 1],
    [2, 3, 4, 2, 16],
    [1, 1, 1, 1, 1]
]
print(znaleziono_ciag(li))
