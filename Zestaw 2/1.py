# Proszę napisać program wczytujący liczbę naturalną i odpowiadający
# na pytanie, czy liczba ta jest iloczynem dowolnych dwóch wyrazów ciągu Fibonacciego

n = int(input("Podaj liczbę naturalną: "))

a, b = 0, 1
found = False
while a * b < n:
    a, b = b, a + b
    if a * b == n:
        print(f"liczba {n} jest iloczynem liczb {a} i {b}")
        found = True

if not found:
    print(f"Liczba n nie jest iloczynem żadnych dwóch kolejnych liczb ciągu fibonacciego")
