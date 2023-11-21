n = int(input("Podaj liczbe: "))

a, b = 1, 1
while a < n:
    if a * b == n:
        print(f"Jest iloczynem {a} i {b}")
    a, b = b, a + b
