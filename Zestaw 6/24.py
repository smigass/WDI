# Zadanie 24. Dana jest lista, który zakonczona jest cyklem. Napisac funkcje, która zwraca liczbe elementów
# przed cyklem.

from Node import Node


def detect_loop(p):
    mem = set()
    while p is not None:
        if p in mem:
            return p
        mem.add(p)
        p = p.next
    return False


def before_cycle_length(p):
    start = detect_loop(p)
    if start:
        cnt = 0
        while p is not None:
            if p is start:
                return cnt
            cnt += 1
            p = p.next
    else:
        return False


# Lista z cyklem
head = Node().fill_with_cycle(4, 2)
head.print_cycle("blue")
print(before_cycle_length(head))

head2 = Node(10)
head2.random_fill(11)
head2.print()
print(before_cycle_length(head2))


