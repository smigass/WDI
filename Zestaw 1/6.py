def f(x):
    return x**x-2020

def bisekcja(a,b):
    fa = f(a)
    fb = f(b)
    if fa * fb > 0:
        return "Błąd"
    while True:
        x0 = a/2 + b/2
        if abs(a - x0) < 0.000000001:
            return a
        if abs(f(x0)) < 0.000000001:
            return f(x0)
        if f(x0)*f(a) < 0:
            b = x0
        else:
            a,fa = x0, f(x0)

print(bisekcja(0,5))
    