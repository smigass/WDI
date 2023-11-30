# Zadanie 13. Napisac program wypisujacy wszystkie mozliwe podziały liczby naturalnej na sume składników.
# Na przykład dla liczby 4 sa to: 1+3, 1+1+2, 1+1+1+1, 2+2.

# Zadanie z zajec z Garkiem (nie dziala)


def rozklad(num, result="", p=1):
    if num == 0:
        print(result[:-1])
    else:
        for i in range(1, num + 1):
            str_i = str(i)
            rozklad(num - i, result + str(i) + "+", i)


rozklad(10)
