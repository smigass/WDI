import random


def listuj(T):
    for i in range(len(T)):
        print(T[i])
    print()

def random_list(n, a):
    return [[random.randint(1, a)for j in range(n)] for i in range(n)]
