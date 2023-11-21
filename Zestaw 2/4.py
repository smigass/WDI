max_bound = int(input("Podaj liczbę N: "))


def find_numbers(max, divisors):
    depth = 1
    flag = True
    found = []
    while flag:
        for i in range(depth):
            good_numbers = 0
            values = [x for x in range(depth + 1)]
            possibilities = [[a, b, c] for a in values for b in values for c in values]
            possibilities = list(filter(lambda x: x if sum(x) == depth else None, possibilities))
            for possibility in possibilities:
                number = 1
                for p in range(len(possibility)):
                    if possibility[p] != 0:
                        number *= divisors[p] ** possibility[p]
                        if number <= max and number not in found:
                            good_numbers += 1
                            found.append(number)
            if good_numbers == 0:
                flag = False
            depth += 1
    return [1, *sorted(found)]


print(find_numbers(max_bound, [2, 3, 5]))
