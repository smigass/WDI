# Zadanie 4. Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Prosze napisac funkcje, która
# zwraca wiersz i kolumne dowolnego elementu, dla którego iloraz sumy elementów w kolumnie w którym lezy
# element do sumy elementów wiersza w którym lezy element jest najwieksza.
import random

from listowanie import listuj


def znajdz_index(t, p):
    index = 0
    for i in range(1, len(t)):
        if p == -1:
            if t[i] < t[index]:
                index = i
        elif p == 1:
            if t[i] > t[index]:
                index = i
    return index

def najwiekszy_iloraz(k,w):
    maximum= (0, 0)
    max_val = k[0] / w[0]
    for i in range(len(k)):
        for j in range(len(w)):
            if w[j] != 0:
                if k[i] / w[j] > max_val:
                   maximum, max_val = (j, i), k[i] / w[j]
    print("max", max_val)
    return maximum



def test(t):
    listuj(t)
    N = len(t)
    sumy_wierszow = [0 for i in range(N)]
    sumy_kolumn = [0 for i in range(N)]
    for i in range(N):
        w, k = 0, 0
        for j in range(N):
            w += t[i][j]
            k += t[j][i]
        sumy_wierszow[i] = w
        sumy_kolumn[i] = k
    print(sumy_kolumn, sumy_wierszow)
    ind = najwiekszy_iloraz(sumy_kolumn, sumy_wierszow)
    return ind

K = 4
T = [[random.randrange(-10, 10) for _ in range(K)] for k in range(K)]
print(test(T))
