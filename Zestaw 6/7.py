# Zadanie 7. Proszę napisac funkcje usuwajaca ostatni element listy. Do funkcji nalezy przekazac wskazanie
# na pierwszy element listy.

from Node import Node


def cut(head: Node):
    p = head
    q = None
    while p.next is not None:
        p, q = p.next, p
    q.next = None
    return head


# Tworzenie nowej listy (niebieska)
ListNode = Node(7)
ListNode.random_fill(20)
ListNode.print()

# Przycinanie ostatniego elementu (zielona)
ListNode = cut(ListNode)
ListNode.print("green")
