def get_divisors(n):
    print("wyk")
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if n / i != i:
                divisors.append(n // i)

    return sorted(divisors)


def get_biggest_common_divisor(a, b, c):
    a_divisors = get_divisors(a)
    b_divisors = get_divisors(b)
    c_divisors = get_divisors(c)
    max_div = 0
    for divisor in a_divisors:
        if divisor in b_divisors and divisor in c_divisors:
            max_div = divisor
    return max_div

print(get_biggest_common_divisor(12,24,48))

