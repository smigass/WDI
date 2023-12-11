import random


def bubble_sort(T):
    n = len(T)
    for i in range(1, n):
        for j in range(n - 1, i - 1, -1):
            if T[j - 1] > T[j]:
                T[j - 1], T[j] = T[j], T[j - 1]
            # end if
        # end for
    # end for
# end def

k = 10
t = [random.randint(1, k * 10) for _ in range(k)]
print(t)
bubble_sort(t)
print(t)