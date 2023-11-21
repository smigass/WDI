number = int(input("Podaj liczbe: "))
number_copy = number
length = 0


while number_copy > 1:
    number_copy /= 10
    length += 1

b = False
last_index = number % 10
number //= 10
for i in range(length):
    if number % 10 == last_index:
        print("NIE")
        b = True
    number //= 10

if not b:
    print("TAK")
