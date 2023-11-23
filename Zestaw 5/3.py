# Zadanie 3. Szachownica jest reprezentowana przez tablice T[8][8] wypełniona liczbami naturalnymi zawierajacymi
# koszt przebywania na danym polu szachownicy. Król szachowy znajduje sie w wierszu 0 i kolumnie
# k. Król musi w dokładnie 7 ruchach dotrzec do wiersza 7. Prosze napisac funkcje, która wyznaczy minimalny
# koszt przejscia króla. Do funkcji nalezy przekazac tablice t oraz startowa kolumne k. Koszt przebywania na
# polu startowym i ostatnim takze wliczamy do kosztu przejscia.
from helpers import *


def find_cheapest_way(t, column, row, cost):
    #cheapest = +math.inf
    if row == 7:
        return cost
    if not 0 <= column <= 7:
        return +math.inf
    cost += t[row][column]
    cost1 = find_cheapest_way(t, column - 1, row + 1, cost)
    cost2 = find_cheapest_way(t, column, row + 1, cost)
    cost3 = find_cheapest_way(t, column + 1, row + 1, cost)

    return min(cost2, cost3, cost1)


T = random_list(8, 9)
listuj(T)
print(find_cheapest_way(T, 4, 0, T[0][4]))
