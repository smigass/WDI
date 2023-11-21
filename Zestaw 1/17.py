import time

start = time.time()


def fibonacci(a, b):
    e = 10 ** (-15)
    last_diff = 0
    while abs((b / a) - last_diff) > e:
        last_diff = b / a
        a, b = b, a + b

    return last_diff


print(fibonacci(12, 130))
end = time.time()

print((end - start), "ms")
