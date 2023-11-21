last_input = ""
numbers = []
while last_input != 0:
    last_input = int(input("Podaj kolejna wartość ciągu: "))
    if last_input != 0:
        numbers.append(last_input)

numbers.sort(reverse=True)
print(numbers[9])
