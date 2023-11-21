from listowanie import random_list, listuj

t1 = [
    [2, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 2, 4, 5],
    [1, 2, 3, 3, 5],
    [1, 2, 3, 4, 4]
]

t = random_list(10, 10)
listuj(t1)


def index_crazy_fib(n):
    if n == 2:
        return 2
    a = 1
    b = 2
    k = 0
    while a <= n:
        if a == n:
            return k
        a, b = b, a + b - 1
        k += 1
    return -1




def seq(T):
    length = len(T)
    max_seq = 1
    curr_seq = 1
    for i in range(length - 3, -(length - 3) - 1 , -1):
        if i >= 0:
            start_point = [0, i]
        else:
            start_point = [-i, 0]
        print(start_point)
        prev = T[start_point[0]][start_point[1]]
        flag = False
        for j in range(1, length - max(start_point[0], start_point[1])):
            el = T[start_point[0] + j][start_point[1] + j]
            prev_index = index_crazy_fib(prev)
            el_index = index_crazy_fib(el)
            if el_index != 2:
                flag = False
            if prev_index == el_index - 1:
                curr_seq += 1
            elif prev_index == 2 and el_index == 2:
                if not flag:
                    curr_seq += 1
                    flag = True
            else:
                if curr_seq > max_seq:
                    max_seq = curr_seq
                    curr_seq = 1
            if j == length - max(start_point[0], start_point[1]) - 1 and curr_seq > max_seq:
                max_seq = curr_seq
                curr_seq = 1
            prev = el
    return max_seq


print(seq(t1))
