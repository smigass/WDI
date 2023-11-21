# Prosze zmodyfikowac wzór Newtona aby program z zadania 5 obliczał pierwiastek stopnia 3

number = int(input("Podaj liczbę n: "))
def get_cbrt(v, eps):
    a = 1
    b = v
    while abs(a - b) > eps:
        a = (2*a + b) / 3
        b = v / a**2
    return a


print(get_cbrt(number, 10 ** (-15)))
print(number**(1/3))
