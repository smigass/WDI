from helpers import *


def find_set(T, s):
    pass


def recursive_search(T, i, l, el_sum=0, ids_sum=0, best_l = math.inf):
    print(i)
    if i == len(T):
        return el_sum == ids_sum, best_l, l

    found, b, length = recursive_search(T, i + 1, l, el_sum, ids_sum, best_l)
    if found and length < best_l:
        best_l = length






t1 = [1, 7, 3, 5, 11, 2]
t = random_linear_list(10, 6)
print(recursive_search(t1, 0))
