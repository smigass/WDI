# Dana jest liczba naturalna N. Proszę zaimplementować funkcję divide(N), która sprawdza czy jest możliwe
# pocięcie liczby N na kawałki, tak aby każdy z kawałków był liczba pierwszą oraz liczba kawałków też była
# liczbą pierwszą. Funkcja powinna zwracać wartość logiczną. Na przykład: divide(2347)=True, podział na
# 23 i 47, natomiast divide(2255)=False
import math


def prime(n: int) -> bool:
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def get_digit(n: int, number: int):
    if number == 0:
        return 0
    N = int(math.log10(number)) + 1
    digit = 0
    for i in range(n):
        digit = number % 10
        number //= 10
    return digit


def divide(n: int, num: int = 0, i: int = 0, p: int = 0) -> bool:
    N = int(math.log10(n)) + 1
    if i == 0:
        num = get_digit(N, n)
    if i == N:
        return prime(p) and prime(num)
    if prime(num):
        return divide(n, get_digit(N - i, n), i + 1, p + 1) or divide(n, num * 10 + get_digit(N - i, n), i + 1, p)
    else:
        return divide(n, num * 10 + get_digit(N - i, n), i + 1, p)


print(divide(100122))
