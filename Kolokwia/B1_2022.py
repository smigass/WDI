import math


def sequence(T):
    n = len(T)
    max_beg, min_end = 0, math.inf
    cur_beg = 0
    cur_len = 1
    for i in range(1, n):
        if T[i] <= T[i - 1]:
            if cur_len > 2:
                if cur_beg > max_beg:
                    max_beg = T[cur_beg]
                if i < min_end:
                    min_end = T[i - 1]
            cur_len = 1
        else:
            if cur_len == 1:
                cur_beg = i - 1
            cur_len += 1
    print(max_beg, min_end)
    if min_end < max_beg:
        return True
    return False


print(sequence([2, 15, 17, 13, 17, 19, 23, 2, 6, 4, 8, 3, 5, 7, 1, 3, 2]))
