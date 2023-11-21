import random

t = [random.randint(1, 1000) for i in range(1, 5)]
print(t)
for number in t:
    faulty = False
    for j in str(number):
        if int(j) % 2 == 0:
            faulty = True
    if not faulty:
        print(number)
