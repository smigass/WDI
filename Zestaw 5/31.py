# Zadanie 31. Prosze napisac funkcje, która jako parametr otrzymuje liczbe naturalna i zwraca sume iloczynów
# elementów wszystkich niepustych podzbiorów zbioru podzielników pierwszych tej liczby. Mozna załozyc,
# ze liczba podzielników pierwszych nie przekracza 20, zatem w pierwszym etapie funkcja powinna wpisac podzielniki do
# tablicy pomocniczej. Przykład: 60 --> [2, 3, 5] --> (2) + (3) + (5) + (2 * 3) + (2 * 5) + (3 * 5) + (2 * 3 * 5) = 71


def get_prime_divisors(n):
    t = []
    for i in range(2, n + 1):
        while n % i == 0:
            n //= i
            if i not in t:
                t += [i]
    return t


def get_sum(n):
    divisors = get_prime_divisors(n)
    s = 0

    def rek(prod=1, depth=0):
        nonlocal s, divisors
        N = len(divisors)
        if depth == N:
            if prod != 1:
                s += prod
        else:
            rek(prod * divisors[depth], depth + 1)
            rek(prod, depth + 1)

    rek()
    return s


print(get_sum(60))
