# Zadanie 23. Dana jest lista, która zakonczona jest cyklem. Napisac funkcje, która zwraca liczbe elementów
# w cyklu.


from Node import Node


def detect_loop(List: Node) -> bool:
    slow, fast = List, List.next
    while slow and fast and slow != fast:
        slow = slow.next
        fast = fast.next.next
    if slow is None or fast is None:
        return False
    p = slow.next
    i = 1
    while p is not fast:
        i += 1
        p = p.next
    return i


# Lista z cyklem
head = Node(10)
head.fill_with_cycle(12, 0)
head.print_cycle("blue")
print(detect_loop(head))

head2 = Node(10)
head2.random_fill(10)
# print(detect_loop(head2))
# head2.print()
