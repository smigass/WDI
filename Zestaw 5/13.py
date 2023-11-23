# Zadanie 13. Napisac program wypisujacy wszystkie mozliwe podziały liczby naturalnej na sume składników.
# Na przykład dla liczby 4 sa to: 1+3, 1+1+2, 1+1+1+1, 2+2.

# TODO - Dokonczyc
def diff(n_tab):
    last_l = list(n_tab)
    if n_tab[-1] > 1:
        n_tab += [0]
    for i in range(len(n_tab) - 1, 0, -1):
        if n_tab[i - 1] > 1:
            n_tab[i] += 1
            n_tab[i - 1] -= 1
            if set(last_l) != set(n_tab):
                for k in range(len(n_tab)):
                    if k != len(n_tab) - 1:
                        print(n_tab[k], end="+")
                    else:
                        print(n_tab[k])
            diff(n_tab)
            break


diff([12])
