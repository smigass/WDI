import random

t = [random.randrange(1,100, 2) for i in range(random.randint(3, 100))]

index = 1
current = 1
max_negative = 0
max_positive = 0
r = t[1] - t[0]

while index < len(t):
    if t[index] - t[index - 1] == r:
        if r > 0:
            current += 1
            if current > max_positive:
                max_positive = current
        elif r < 0:
            current += 1
            if current > max_negative:
                max_negative = current
    else:
        r = t[index] - t[index - 1]
        current = 2
        if r > 0:
            if current > max_positive:
                max_positive = current
        elif r < 0:
            if current > max_negative:
                max_negative = current
    index += 1
print(t)
print(max_positive - max_negative)