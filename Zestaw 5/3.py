# Zadanie 3. Szachownica jest reprezentowana przez tablice T[8][8] wypełniona liczbami naturalnymi zawierajacymi
# koszt przebywania na danym polu szachownicy. Król szachowy znajduje sie w wierszu 0 i kolumnie
# k. Król musi w dokładnie 7 ruchach dotrzec do wiersza 7. Prosze napisac funkcje, która wyznaczy minimalny
# koszt przejscia króla. Do funkcji nalezy przekazac tablice t oraz startowa kolumne k. Koszt przebywania na
# polu startowym i ostatnim takze wliczamy do kosztu przejscia.
from helpers import *


def king(t, col, cost=0, row=0):
    # cheapest = +math.inf
    if row == 7:
        return t[row][col]
    if not 0 <= col <= 7:
        return +math.inf
    cost1 = king(t, col - 1, cost + t[row + 1][col - 1], row + 1)
    cost2 = king(t, col, cost + t[row + 1][col], row + 1)
    cost3 = king(t, col + 1, cost + t[row + 1][col + 1], row + 1)

    return t[row][col] + min(cost2, cost3, cost1)


T = random_list(8, 20)
listuj(T)
print(king(T, 0, T[0][0]))
