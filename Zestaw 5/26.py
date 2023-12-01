# Zadanie 26. Do budowy liczby naturalnej reprezentowanej w systemie dwójkowym mozemy uzyc A cyfr
# 1 oraz B cyfr 0, gdzie A, B > 0. Proszę napisac funkcje, która dla zadanych parametrów A i B zwraca ilosc
# wszystkich mozliwych do zbudowania liczb, takich z pierwsza cyfra w systemie dwójkowym (najstarszy
# bit) jest równa 1, a zbudowana liczba jest złozona. Na przykład dla A = 2, B = 3 ilosc liczb wynosi 3, są to
# 10010(2), 10100(2), 11000(2)

from helpers import is_prime, to_decimal


def build_numbers(A, B):
    counter = 0

    def build(A, B, number=1):
        nonlocal counter
        if A == 0 and B == 0:
            if not is_prime(to_decimal(number, 2)):
                counter += 1
                return 0
        if A != 0:
            build(A - 1, B, number * 10 + 1)
        if B != 0:
            build(A, B - 1, number * 10)

    build(A - 1, B)
    return counter


print(build_numbers(2, 3))
