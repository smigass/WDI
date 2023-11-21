import math


def sequence(T):
    n = len(T)
    max_beg, min_end = 0, float(math.inf)
    i = 1
    while i < n:
        cnt = 1
        beg = T[i - 1]
        while i < n and T[i - 1] < T[i]:
            print(i)
            i += 1
            cnt += 1
        end = T[i - 1]
        print(end)
        if cnt > 2:
            max_beg = max(beg, max_beg)
            min_end = min(end, min_end)
        i += 1
        print(max_beg, min_end)
    return max_beg > min_end

print(sequence([2, 15, 17, 13, 17, 19, 23, 2, 6, 4, 8, 3, 5, 7, 14, 3, 2]))