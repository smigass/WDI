# Zadanie 17. Proszę napisac funkcje, która otrzymujac jako parametr wskazujacy na poczatek listy dwukierunkowej,
# usuwa z niej wszystkie elementy, w których wartosc klucza w zapisie binarnym ma nieparzysta
# ilosc jedynek.
import random

from LinkedList import LinkedList


def odd(n: int) -> bool:
    cnt = 0
    while n != 0:
        cnt += n % 2
        n //= 2
    return cnt % 2 == 1


def to_binary(n):
    binary = 0
    i = 0
    while n != 0:
        binary += (n % 2) * 10 ** i
        i += 1
        n //= 2
    return binary


def remove(node: LinkedList) -> LinkedList:
    p = node
    last = None
    while p is not None:
        if odd(p.val):
            if p.prev:
                last = p.prev if last is None else last
            else:
                node = p.next
        elif last:
            last.next = p
            last = None
        p = p.next
    if last:
        last.next = p
    return node


# Listy z ktorych tworza się linked listy jedna losowa i druga ta sama tylko binarnie
T = [random.randint(1, 100) for i in range(10)]
T_B = [to_binary(T[i]) for i in range(len(T))]

# Lista przed usunieciem (niebieska)
head = LinkedList(25)
head.fill_with_list(T)
head.print()

# Lista z liczbami zapisanymi binarnie (zolta)
binary_head = LinkedList(to_binary(25))
binary_head = binary_head.fill_with_list(T_B)
binary_head.print("yellow")

# Lista po usunieciu liczb spelniajacych warunki zadania (zielona)
remove(head).print("green")
