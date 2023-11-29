# Zadanie 3. Szachownica jest reprezentowana przez tablice T[8][8] wypełniona liczbami naturalnymi zawierajacymi
# koszt przebywania na danym polu szachownicy. Król szachowy znajduje sie w wierszu 0 i kolumnie
# k. Król musi w dokładnie 7 ruchach dotrzec do wiersza 7. Prosze napisac funkcje, która wyznaczy minimalny
# koszt przejscia króla. Do funkcji nalezy przekazac tablice t oraz startowa kolumne k. Koszt przebywania na
# polu startowym i ostatnim takze wliczamy do kosztu przejscia.

# Rozwiazanie alternatywne - robione na ćwiczeniach z Garkiem


from helpers import *


def find_cheapest_way(T, k):
    def king(t, col, row=0, cost=0):
        nonlocal min_cost
        if row == 7:
            min_cost = min(min_cost, cost)
            return 0
        if col > 0:
            king(t, col - 1, row + 1, cost + t[row + 1][col - 1])
        if col < len(T) - 1:
            king(t, col + 1, row + 1, cost + t[row + 1][col + 1])
        king(t, col, row + 1, cost + t[row + 1][col])

    min_cost = +math.inf
    king(T, k)
    return min_cost + T[0][k]


T = random_list(8, 20)
list_table(T)

print(find_cheapest_way(T, 0))
