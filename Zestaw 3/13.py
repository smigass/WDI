import random

t = [2, 9, 3, 1, 7, 11, 9, 6, 7, 7, 1, 3, 9, 12, 15]
t_reversed = list(reversed(t))
print(t_reversed)

current_length = len(t) - 1

while current_length > 0:
    steps = 0
    for i in range(len(t) + 1 - current_length):
        s = t[steps:current_length + steps]
        if " " + str(s)[1:-1] in str(t_reversed):
            print(current_length)
        steps += 1
    current_length -= 1
