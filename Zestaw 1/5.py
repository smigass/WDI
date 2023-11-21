def get_sqrt(n, eps):
    a = 1
    b = n
    while abs(a - b) > eps:
        a = (a+b)/2
        b = n/a
    return a

number = 12
print(number**0.5)
print(get_sqrt(number, 10**(-10)))