T1 = [
    [0, 0, 1, 1],
    [1, 0, 1, 1],
    [1, 0, 0, 0],
    [0, 0, 1, 1]
]


def is_odd(n):
    l = 0
    while n != 0:
        l += n % 2
        n //= 2
    return l % 2


def check(T):
    N = len(T)
    not_odds = []
    for i in range(N):
        for j in range(N):
            if not is_odd(T[i][j]):
                not_odds += [(i, j)]
    wrong_cols = [not_odds[i][1] for i in range(len(not_odds))]
    wrong_rows = [not_odds[i][0] for i in range(len(not_odds))]
    for i in range(len(set(wrong_cols))):
        for j in range(i, len(set(wrong_cols))):
            for wr in set(wrong_rows):
                cnt = 0
                for v in not_odds:
                    if v[1] == i or v[1] == j or v[0] == wr:
                        cnt += 1
                if cnt == len(not_odds):
                    return True
    return False


print(check(T1))
