import random


def get_maximum_progression(t):
    print(t)
    index = 1
    maximum = 0
    current = 1
    r = t[1] - t[0]
    while index < len(t):
        if t[index] - t[index - 1] == r:
            current += 1
            if current > maximum:
                maximum = current
        else:
            r = t[index] - t[index - 1]
            current = 2
        index += 1

    return maximum


print(get_maximum_progression([1,2,3,4,7,8,9,10,11,12,14]))

