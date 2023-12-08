# Zadanie 27. Kwadrat jest opisywany czwórka liczb całkowitych (x1, x2, y1, y2), gdzie x1, x2, y1, y2 oznaczaja
# proste ograniczajace kwadrat x1 < x2, y1 < y2. Dana jest tablica T zawierajaca opisy N kwadratów. Proszę
# napisac funkcje, która zwraca wartosc logiczna True, jesli danej tablicy mozna znalezc 13 nienachodzacych
# na siebie kwadratów, których suma pól jest równa 2012 i False w przeciwnym przypadku.
import math
import random


def get_field(sq):
    return math.ceil(abs(sq[0] - sq[1]) * abs(sq[2] - sq[3]))


def check(T, index=0, s=2012, used=[]):
    N = len(T)
    if len(used) == 12:
        if s == 0:
            return True
        return False
    if index == N:
        return False
    ovr = False
    if s - get_field(T[index]) < 0:
        ovr = True
    for sq in used:
        if overrunning(T[index], sq):
            ovr = True
    if ovr:
        return check(T, index + 1, s, used)
    return check(T, index + 1, s, used) or check(T, index + 1, s - get_field(T[index]), [*used, T[index]])


def overrunning(sq1, sq2):
    for p in get_points(sq1):
        if in_square(p, sq2):
            return True
    return False


def in_square(point, sq):
    if sq[0] <= point[0] <= sq[1]:
        if sq[2] <= point[1] <= sq[3]:
            return True
    return False


def get_points(sq):
    return [(sq[0], sq[2]), (sq[0], sq[3]), (sq[1], sq[2]), (sq[1], sq[3])]


def g():
    return random.randint(-100, 100)


# Przyklad tablicy ktora spelnia warunki zadania
# tablica 13 kwadratow spelniajacych kryteria zadania
h = []
k = 0
for i in range(12):
    h.append((0 + k, 1 + k, 0 + k, 1 + k))
    k += 1.2
h.append((1000, 1000 + math.sqrt(2000), 1000, 1000 + math.sqrt(2000)))

# losowe 20 innych kwadratów
T = [(g(), g(), g(), g()) for i in range(20)]
T = [*T, *h]

print(check(T))
