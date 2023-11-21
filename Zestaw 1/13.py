def nww(a,b,c):
    a1, b1, c1 = a, b, c
    while a1 != b1 or b1 != c1:
        minimum = min([a1,b1,c1])
        if minimum == a1: a1 += a
        elif minimum == b1: b1 += b
        elif minimum == c1: c1 += c
    return a1

print(nww(56,45,156))