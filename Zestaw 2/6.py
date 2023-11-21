def decomposition(n):
    step = 1
    a = 1
    b = a + step
    while a * b != n:
        a += 1
        b = a + step
        if a * b > n:
            step += 1
            a = 1
            b = a + step
    return (a, b)

print(decomposition(80672138))