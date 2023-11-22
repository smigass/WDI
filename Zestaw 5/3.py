# Zadanie 3. Szachownica jest reprezentowana przez tablice T[8][8] wypełniona liczbami naturalnymi zawierajacymi
# koszt przebywania na danym polu szachownicy. Król szachowy znajduje sie w wierszu 0 i kolumnie
# k. Król musi w dokładnie 7 ruchach dotrzec do wiersza 7. Prosze napisac funkcje, która wyznaczy minimalny
# koszt przejscia króla. Do funkcji nalezy przekazac tablice t oraz startowa kolumne k. Koszt przebywania na
# polu startowym i ostatnim takze wliczamy do kosztu przejscia.
from helpers import *


def find_cheapest_way(t, column, row, cost):
    cheapest = +math.inf
    if row + 1 == 8:
        return cost
    for i in range(column - 1, column + 2):
        if t[row + 1][i] < cheapest:
            if 8 > i >= 0:
                cheapest = t[row + 1][i]
    return find_cheapest_way(t, column, row + 1, cost + cheapest)


T = random_list(8, 9)
listuj(T)
print(find_cheapest_way(T, 4, 0, T[0][4]))
