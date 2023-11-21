def check(t):
    minimum = t[0]
    maximum = t[0]
    max_counter = 0
    min_counter = 0
    for i in range(1, len(t)):
        if t[i] < minimum:
            minimum = t[i]
            max_counter = 1
        elif t[i] == minimum:
            min_counter += 1
        if t[i] > maximum:
            maximum = t[i]
            min_counter = 1
        elif t[i] == maximum:
            max_counter += 1
    if min_counter == 1 and max_counter == 1:
        return True
    else: return False

print(check([-1, -2, 2, 5, 4]))
