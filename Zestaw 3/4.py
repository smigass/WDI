def silnia(n):
    s = 1
    for i in range(1, n + 1):
        s *= i
    return s


def euler(n):
    c = 0
    k = 10
    tab = [0 for i in range(n + k)]
    for i in range(n + 100):
        t = [0 for k in range(n + k)]
        a = 1
        b = silnia(i)
        c += a // b
        for j in range(n + k):
            a %= b
            a *= 10
            t[j] = a // b
        for j in range(n + k):
            tab[n - 1 - j] += t[n - 1 - j]
            if tab[n - 1 - j] >= 10:
                # print(tab[n - 2 - j], tab[n - 1 - j])
                tab[n - 2 - j] += 1
                tab[n - 1 - j] = tab[n - 1 - j] % 10
                # print(tab[n - 2 - j], tab[n - 1 - j])
    return str(c) + "." + "".join([*[str(x) for x in tab[:n - 1]], str(tab[n - 1]) if tab[n] < 5 else str(tab[n - 1] + 1)])


print(euler(290))
