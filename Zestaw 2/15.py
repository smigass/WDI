import time

n = int(input("Podaj liczbe n: "))
start = time.time()
for number in range(10 ** (n - 1), 10 ** n):
    number_ = number
    s = 0
    for i in range(n):
        s += (number_ % 10) ** n
        number_ //= 10
    if s == number:
        print(number)
end = time.time()

print((end - start) * 10**3, "ms")