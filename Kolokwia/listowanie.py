import random


def listuj(T):
    print()
    for i in range(len(T)):
        for j in range(len(T)):
            print(T[i][j], end='\t')
        print('')
    print()

def random_list(n, a):
    return [[random.randint(1, a)for j in range(n)] for i in range(n)]
