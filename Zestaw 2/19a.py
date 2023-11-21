def ile25(n):
    d = 0
    p = 0
    while n % 2 == 0:
        d += 1
        n //= 2
    while n % 5 == 0:
        p += 1
        n //= 5
    return max(d, p)


def okres(l, m):
    print(l // m, end="")
    l %= m
    if l != 0:
        print(".", end="")
        for i in range(ile25(m)):
            l *= 10
            print(l // m, end="")
            l %= m
        # end
        if l != 0:
            print("(", end="")
            r = l
            while True:
                l *= 10
                print(l // m, end="")
                l %= m
                if l == r:
                    break
            print(")")
            # end

okres(3, 7)