number = int(input("Podaj sumę: "))


def test(n):
    a, b = 1, 1
    s = 0
    while s <= n:
        if s == n:
            return "Istnieje taki ciąg"
        s += a
        a, b = b, a + b

    a, b = 1, 1
    while s >= n:
        if s == n:
            return "Istnieje taki ciąg"
        s -= a
        a, b = b, a + b
    return "Nie istnieje taki ciąg"


print(test(number))
