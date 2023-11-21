number = int(input("Podaj liczbę n: "))


def get_next(n):
    for i in range(n + 1, 1000):
        flag = False
        a, b = 1, 1
        s = 0
        while s <= i:
            if s == i:
                flag = True
            s += a
            a, b = b, a + b

        a, b = 1, 1
        while s >= i:
            if s == i:
                flag = True
            s -= a
            a, b = b, a + b
        if not flag: return i
        

print(get_next(number))
