import random


def selection_sort(T):
    n = len(T)
    for i in range(0, n - 1):
        nm = i
        for j in range(i + 1, n):
            if T[j] < T[nm]:
                nm = j
        # end for
        T[nm], T[i] = T[i], T[nm]
    # end for
# end def

k = 1000
t = [random.randint(1, k * 10) for _ in range(k)]
print(t)
selection_sort(t)
print(t)
