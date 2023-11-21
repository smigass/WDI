t = [i for i in range(1, 1001)]

for number in t:
    faulty = True
    for j in [1, 3, 5, 7, 9]:
        if str(j) in str(number):
            faulty = False
    if faulty:
        print(number)
