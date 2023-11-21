number = int(input("Podaj liczbe: "))

if number / 10 ** 9 > 1:
    print("NIE")

b = False
for i in range(len(str(number)) - 1, 0, -1):
    last = number % 10
    first = ((number - number % 10) // 10) % 10
    if last <= first:
        b = True
        print("NIE")
        break
    number = number// 10
if not b:
    print("TAK")
