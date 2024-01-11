# Zadanie 23. Dana jest lista, która zakonczona jest cyklem. Napisac funkcje, która zwraca liczbe elementów
# w cyklu.


from Node import Node


def detect_loop(p):
    mem = set()
    while p is not None:
        if p in mem:
            return p
        mem.add(p)
        p = p.next
    return False


def cycle_length(p):
    p = detect_loop(p)
    if p:
        k = p.next
        cnt = 1
        while k is not p:
            k = k.next
            cnt += 1
        return cnt
    else:
        return False


# Lista z cyklem
head = Node(10)
head.fill_with_cycle(12, 3)
head.print_cycle("blue")
print(cycle_length(head))

head2 = Node(10)
head2.random_fill(11)
head2.print()
print(cycle_length(head2))
