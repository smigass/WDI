# Zadanie 22. Dana jest lista, która byc moze zakonczona jest cyklem. Napisac funkcje, która sprawdza
# ten fakt.


from Node import Node


# Rozwiazanie 2
def detect_loop(p: Node) -> bool:
    mem = set()
    while p is not None:
        if p in mem:
            return True
        mem.add(p)
        p = p.next
    return False


# Lista z cyklem
head = Node(10)
head.fill_with_cycle(5, 7)
head.print_cycle()
print(detect_loop(head))

head2 = Node(10)
head2.random_fill(10)
head2.print()
print(detect_loop(head2))

