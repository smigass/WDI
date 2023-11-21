def integral(eps, k, step):
    x = 1
    field = 0
    while x + step < k:
        x += step
        y = 1 / x
        last_field = step * y
        field += last_field
    return field


print(integral(10 ** (-10), 10000, 0.001))
