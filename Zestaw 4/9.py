from listowanie import *


def znajdz_kwadrat(T, k):
    listuj(T)
    for i in range(3, len(T), 2):
        for x in range(i - 1, len(T)):
            for y in range(0, len(T) - (i - 1)):
                suma = T[x][y] + T[x - (i - 1)][y] + T[x - (i - 1)][y + (i - 1)] + T[x][y + (i - 1)]
                if suma == k:
                    return (x - (i - 1)//2, y + (i - 1)//2), "dlugosc boku: " + str(i)


print(znajdz_kwadrat(random_list(50, 15), 82))
