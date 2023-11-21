def silnia(n): return silnia(n - 1) * n if n > 1 else 1


def euler(precision):
    last_e_element = precision + 1
    e = 0
    i = 0
    while last_e_element > precision:
        last_e_element = 1 / silnia(i)
        e += last_e_element
        i += 1
    return e

def e(p):
    e = 0
    for i in range(p):
        e += 1/silnia(i)
    return e

print(e(500))


#print(euler(10 ** (-10)))
