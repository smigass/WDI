digits_10 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
digits_16 = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F")

dictionary = {digits_10[i]: digits_16[i] for i in range(len(digits_10))}


def change_system(s, n):
    tab = []
    while n != 0:
        tab.append(dictionary[n % s])
        n //= s
    return "".join(list(reversed(tab)))



a = 7594
b = 9734

found = False
for i in range(2, 17):
    flag = True
    changed_a = change_system(i, a)
    changed_b = change_system(i, b)
    for k in range(i):
        if dictionary[k] in changed_a and dictionary[k] in changed_b:
            flag = False
    if flag:
        print(f'System: {i}\nWartość a: {changed_a}\nWartość b: {changed_b}')
        found = True
        break

if not found:
    print("Nie ma takiego systemu")
