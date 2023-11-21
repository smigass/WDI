number = int(input("Podaj liczbe: "))
number_copy = number
length = 0
while number_copy > 1:
    number_copy /= 10
    length += 1

b = False
for i in range(length):
    last_index = number%10
    if last_index == length:
        print("TAK")
        b = True
    number //= 10

if not b:
    print("NIE")

