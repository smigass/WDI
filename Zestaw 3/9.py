import random


def get_maximum_progression(t):
    print(t)
    index = 1
    maximum = 0
    current = 1
    while index < len(t):
        if t[index] > t[index - 1]:
            current += 1
        else:
            if current > maximum:
                maximum = current
            current = 1
        index += 1

    return maximum


print(get_maximum_progression([random.randint(1, 1000) for i in range(random.randint(1, 10))]))

