number_1 = input("Podaj liczbę 1: ")
number_2 = input("Podaj liczbę 2: ")


def is_similar(a, b):
    list_a = [a[i] for i in range(len(str(a)))]
    list_b = [b[i] for i in range(len(str(b)))]
    if set(list_a) == set(list_b):
        for n in set(list_a):
            if list_a.count(n) != list_b.count(n):
                return False
        return True
    else:
        return False


print(is_similar(number_1, number_2))
