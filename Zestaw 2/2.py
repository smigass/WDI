ab = input("Podaj dzielenie [<a>/<b>]: ")
a, b = ab.split('/')
a, b = int(a), int(b)
n = int(input("Ile miejsc po przecinku?: "))

print(a // b, end=".")

for i in range(n):
    a %= b
    a *= 10
    print(a // b, end="")
