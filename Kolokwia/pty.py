def nwd(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def trojki(T: list) -> int:
    N = len(T)
    counter = 0

    def search(ind: int = 0, space: int = 0, numbers: list = []) -> int:
        # print(ind, numbers)
        nonlocal T, counter
        if len(numbers) == 3 and space < 3:
            counter += 1
            print(numbers)
            return 0
        if space > 2 or ind == len(T):
            return 0
        can_add = True
        for n in numbers:
            if nwd(n, T[ind]) != 1:
                can_add = False
        if can_add:
            search(ind + 1, 1, numbers + [T[ind]])
            if len(numbers) == 0:
                search(ind + 1, 1, numbers)
            else:
                search(ind + 1, space + 1, numbers)

        else:
            search(ind + 1, space + 1, numbers)

    search()
    return counter


print(trojki([2, 4, 3, 6, 5, 3, 5, 23, 2, 2, 45, 2, 3, 523, 5, 32, 2, 5, 2, 52, 5, 2213, 3, 2, 5, 1, 4, 5, 1, 5]))
