import random


def insertion_sort(T):
    n = len(T)
    for i in range(2, n):
        print(T)
        x = T[i]
        T[0] = x  # wartownik
        j = i - 1
        while x < T[j]:
            T[j + 1] = T[j]
            j -= 1
        # end while
        T[j + 1] = x
    # end for
# end def



k = 10
t = [random.randint(1, k * 10) for _ in range(k)]
print(t)
insertion_sort(t)
print(t)

