# Zadanie 4 (5 pkt) W tablicy o rozmiarze N ×N wypełnionej liczbami naturalnymi umieszczono dokładnie jeden fragment
# ciągu Fibonacciego o długości co najmniej 3 elementy. Cały fragment leży w jednym z wierszy lub kolumn w kierunku
# rosnącym, lub malejącym. Proszę napisać funkcję, która dla zadanej tablicy odszuka ten fragment i zwróci jego wartość.

from listowanie import listuj, random_list


def fib_ind(N):
    a, b = 0, 1
    cnt = 0
    while True:
        if a == N:
            return cnt
        if a > N:
            return False
        a, b = b, b + a
        cnt += 1

def reverse_tab(T):
    return [[T[i][j] for i in range(len(T))] for j in range(len(T))]

def check(T):
    N = len(T)
    #listuj(T)
    for row in range(N):
        cnt_a, cnt_b = 0, 0
        last_a, last_b = -10, -10
        hist_a = []
        hist_b = []
        for i in range(N):
            val_a = T[row][i]
            val_b = T[row][N - 1 - i]
            #print(val_a, val_b)
            if fib_ind(val_a) == last_a + 1:
                #print("b", cnt_a)
                cnt_a += 1
                hist_a += [val_a]
                last_a += 1
            elif fib_ind(val_a) != last_a + 1:
                if cnt_a > 3:
                    return hist_a
                elif fib_ind(val_a):
                    #print('A')
                    cnt_a = 1
                    last_a = fib_ind(val_a)
                    hist_a = [val_a]
                else:
                    hist_a, cnt_a = [], 0
            if fib_ind(val_b) == last_b - 1:
                cnt_b += 1
                hist_b += [val_b]
                last_b += 1
            elif fib_ind(val_b) != last_b - 1:
                if cnt_b > 3:
                    return hist_b
                elif fib_ind(val_b):
                    cnt_b = 1
                    hist_b = [val_b]
                    last_b = fib_ind(val_b)
                else:
                    hist_b, cnt_b = [], 0

        if cnt_a > 3:
            return hist_a
        if cnt_b > 3:
            return hist_b


t = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [2, 3, 2, 8, 1],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
]

t1 = random_list(100, 20)

print(check(t1))
print(check(reverse_tab(t1)))
