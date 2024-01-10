# Zadanie 22. Dana jest lista, która byc moze zakonczona jest cyklem. Napisac funkcje, która sprawdza
# ten fakt.


from Node import Node


def detect_loop(List: Node) -> bool:
    slow, fast = List, List.next
    while slow and fast and slow != fast:
        if slow.next == slow:
            return True
        else:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
    return slow == fast


# Lista z cyklem
head = Node(10)
head.fill_with_cycle(5, 7)
head.print_cycle()
print(detect_loop(head))

# head2 = Node(10)
# head2.random_fill(10)
# print(detect_loop(head2))
# head2.print()
