# Zadanie 13. Napisac program wypisujacy wszystkie mozliwe podziały liczby naturalnej na sume składników.
# Na przykład dla liczby 4 sa to: 1+3, 1+1+2, 1+1+1+1, 2+2.

# TODO - dokończyć
def diff(n):
    if n == 1:
        print(1, end="+")
    else:
        for i in range(1, n):
            diff(n - i)
            if i == n - 1:
                print(i)
            else:
                print(i)


diff(4)
