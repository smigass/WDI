i = 0


def get_a_value(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
         return get_a_value(n - 1) - get_b_value(n - 1) * get_a_value(n - 2)


def get_b_value(n):
    if n == 0:
        return 2
    else:
        return get_b_value(n - 1) + 2 * get_a_value(n - 1)


flag = True

for j in range(10):
    print(j, get_a_value(j))

while flag:
    last_input = int(input("Podaj kolejny wyraz ciągu A: "))
    if last_input == get_a_value(i):
        print(get_b_value(i))
        i += 1
    else:
        flag = False
