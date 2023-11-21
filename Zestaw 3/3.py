import time

start = time.time()


def eratostens(n):
    primes = [i for i in range(1, n)]
    index = 1
    while primes[index] < n ** 0.5:
        p = 2
        while primes[index] * p <= n:
            if primes[index] * p in primes:
                primes.remove(primes[index] * p)
            p += 1
        index += 1
    return primes[1:]

print(eratostens(13))

end = time.time()
print((end - start) * 10 ** 3, "ms")
