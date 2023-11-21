import random


def experiment(n, iterations):
    same_days = 0
    for i in range(iterations):
        same_day = False
        people = [random.randint(1, 365) for i in range(n)]
        people_set = set(people)
        if len(people_set) != len(people):
            same_day = True
        if same_day:
            same_days += 1

    return same_days / iterations


print(experiment(23, 100000))
