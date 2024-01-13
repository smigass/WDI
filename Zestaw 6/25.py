# Zadanie 25. Dana jest lista, który zakonczona jest cyklem. Napisac funkcje, która zwraca wskaznik do
# ostatniego elementu przed cyklem.

from Node import Node


def get_last_before_cycle(p):
    if p is None:
        return None
    mem = []
    while p is not None:
        if p in mem:
            print(mem[mem.index(p) - 1].val)
            return mem[mem.index(p) - 1]
        mem.append(p)
        p = p.next
    return False


# Lista z cyklem
head = Node().fill_with_cycle(12, 2)
head.print_cycle("blue")
print(get_last_before_cycle(head))

head2 = Node(10)
head2.random_fill(11)
head2.print()
print(get_last_before_cycle(head2))
