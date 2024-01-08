# „Obcięcie” liczby naturalnej polega na usunięciu z niej M początkowych i N końcowych cyfr, gdzie
# M, N ⩾ 0. Proszę napisać funkcję, która dla danej liczby naturalnej K zwraca największą liczbę
# pierwszą o różnych cyfrach, jaką można uzyskać z obcięcia liczby K albo 0, gdy taka liczba nie
# istnieje. Na przykład dla liczby 1202742516 spośród obciętych liczb pierwszych: 2, 5, 7, 251, 2027
# liczbą spełniającą warunek jest liczba 251.
import math


def number_to_list(k):
    l = int(math.log10(k)) + 1
    t = [0 for i in range(l)]
    for i in range(l):
        last_digit = k % 10
        t[l - 1 - i] = last_digit
        k //= 10
    return t


def list_to_number(T):
    num = 0
    for i in range(0, len(T)):
        num += T[i] * 10 ** (len(T) - i - 1)
    return num


def different_digits(T):
    t = [0 for i in range(10)]
    for v in T:
        if t[v] == 1:
            return False
        t[v] += 1
    return True


def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def prime(k):
    tab = number_to_list(k)
    found = False
    n = len(tab)
    current_length = n
    while not found:
        for i in range(0, n - current_length + 1):
            if different_digits(tab[i:i + current_length]):
                number = list_to_number(tab[i:i + current_length])
                if is_prime(number):
                    return number
        current_length -= 1


print(prime(1202742516))
