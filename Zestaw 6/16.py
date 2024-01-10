# Zadanie 16. Proszę napisac funkcje, która otrzymujac jako parametr wskazujacy na poczatek listy jednokierunkowej,
# przenosi na poczatek listy te z nich, które mają parzysta ilosc piątek w zapisie ósemkowym.
import random

from Node import Node


# Zamiana liczby na system ósemkowy do testowania (do zielonej listy)
def to_oct(n):
    t = 0
    i = 0
    while n != 0:
        t += (n % 8) * 10 ** i
        i += 1
        n //= 8
    return t


def octagonal(number: int) -> bool:
    tab = [0 for i in range(8)]
    while number != 0:
        k = number % 8
        tab[k] += 1
        number //= 8
    return tab[5] % 2 == 0 and tab[5] != 0  # zakladam z liczba 5 w liczbie musi byc parzysta i wieksza od 0


def convert(head: Node) -> Node:
    p, q = head.next, head
    while p is not None:
        if p == q:
            p = p.next
        if octagonal(p.val):
            q.next = p.next
            p.next = head
            head, p = p, q
        p, q = p.next, p
    return head


# Odsylaczowa z listy (niebieska)
T = [random.randint(1, 10000) for i in range(10)]
ListNode = Node(1902).fill_with_list(T)
ListNode.print()

# Pogladowa odsyłaczowa z zamienionymi elementami na system ósemkowy (zielona)
copy = Node(to_oct(1902)).fill_with_list([to_oct(T[i]) for i in range(len(T))])
copy.print("green")

# Po przesunięciu elementów (zolta)
convert(ListNode).print("yellow")
