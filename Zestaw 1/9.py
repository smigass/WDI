def podzielniki(number):
    tab = []
    for i in range(1, int(number / 2) + 1):
        if number % i == 0:
            tab.append(i)

    return [*tab, number]


print(podzielniki(27))
