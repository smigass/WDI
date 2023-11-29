# Zadanie 13. Napisac program wypisujacy wszystkie mozliwe podziały liczby naturalnej na sume składników.
# Na przykład dla liczby 4 sa to: 1+3, 1+1+2, 1+1+1+1, 2+2.

def diff(num, rem_s, k, el=[]):
    # print(n, rem_s,k , el)
    if rem_s == 0:
        if len(el) != 1:
            print("+".join([str(v) for v in el]))
        return 0
    if k == 1:
        diff(num, rem_s - 1, k, el + [1])
    elif rem_s < k:
        diff(num, rem_s, rem_s, el)
    else:
        diff(num, rem_s, k - 1, el)
        diff(num, rem_s - k, k, el + [k])


n = 6
diff(n, n, n)
