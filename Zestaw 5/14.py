# Zadanie 14. Problem wiez w Hanoi (tresc oczywista)
def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n - 1, a, c, b)
        print(f'{a} ➞ {c}')
        hanoi(n - 1, b, a, c)


hanoi(4, "A", "B", "C")
