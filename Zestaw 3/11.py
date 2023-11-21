import random


def get_maximum_progression(t):
    print(t)
    index = 1
    maximum = 0
    current = 1
    q = t[1] / t[0]
    while index < len(t):
        if t[index] / t[index - 1] == q:
            current += 1
            if current > maximum:
                maximum = current
        else:
            q = t[index] / t[index - 1]
            current = 1
        index += 1

    return maximum


print(get_maximum_progression([1,1,2,4,8,16,2]))

