number = int(input("Podaj liczbę n: "))


def get_term(n):
    if n == 1:
        return 2
    return 3 * n + 1


def is_muliple(n):
    i = 1
    last = 0
    while last < n:
        last_value = get_term(i)
        print(last_value)
        j = 0
        while last < n:
            last += last_value
            j += 1
            if last == n:
                return i, j
        i += 1
        j = 0
        last = 0
        if last == n:
            return i, j

    return False


print(is_muliple(number))
