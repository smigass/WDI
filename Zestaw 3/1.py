digits_10 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
digits_16 = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')

dictionary = {digits_10[i]: digits_16[i] for i in range(len(digits_10))}


def change_system(n, s):
    tab = []
    while n != 0:
        tab.append(digits_16[n % s].lower())
        n //= s
    if s == 16:
        return "#" + "".join(reversed(tab))
    return "".join(reversed(tab))


print(change_system(255, 16))
