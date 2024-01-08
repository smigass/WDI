# Zadanie 2. Zastosowanie listy odsyłaczowej do implementacji tablicy rzadkiej. Proszę napisac trzy funkcje:
# – inicjalizujaca tablice – zwracajaca wartosc elementu o indeksie n. – podstawiajaca wartosc value pod indeks
# n.


from Node import *


def initialize(n):
    h = Node(0)
    p = h
    for i in range(n - 1):
        n = Node(0)
        p.next = n
        p = n
    return h


def get_value(list, n):
    p = list
    for i in range(n):
        if p.next is None:
            return False
        p = p.next
    return p.val


def set_val(list, n, val):
    p = list
    for i in range(n):
        if p.next is None:
            return False
        p = p.next
    p.val = val


head = initialize(10)
head.print()
set_val(head, 0, 23)
set_val(head, 9, 22)
head.print()
print(get_value(head, 0))
