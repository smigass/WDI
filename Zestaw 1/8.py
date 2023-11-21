import math

n = int(input("Podaj liczbę: "))


def is_prime(number):
    if number == 2:
        return True
    if number == 1 or number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True

print(is_prime(n))
