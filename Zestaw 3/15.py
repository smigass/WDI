def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def check(t):
    a = 1
    b = 1
    found_prime = False
    for i in range(1, len(t) - 1):
        if i == b:
            a, b = b, a + b
            if is_prime(t[i]):
                return False
        else:
            if is_prime(t[i]):
                found_prime = True
    return found_prime


print(check([2, 4, 6, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
