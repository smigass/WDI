import time

primes = []

start = time.time()
def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for j in range(3, int(n ** 0.5) + 1, 2):
        if n % j == 0:
            return False
    return True


def get_primes(n):
    p = []
    count = 0
    s = 0
    while n != 1:
        if n % primes[count] == 0:
            s1 = get_digits_sum(primes[count])
            s += s1
            n //= primes[count]
            count = 0
        else:
            count += 1
    return s


def get_digits_sum(number):
    s = 0
    while number > 0:
        s += number % 10
        number //= 10

    return s


for i in range(1, 1000000):
    if is_prime(i):
        primes.append(i)

for j in range(1, 1000000):
    if not is_prime(j):
        p_sum = get_primes(j)
        d_sum = get_digits_sum(j)
        if p_sum == d_sum:
            print(j)

finish = time.time()

print((finish - start)* 10**3, 'ms')