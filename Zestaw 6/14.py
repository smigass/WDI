# Zadanie 14. Proszę napisac funkcje, otrzymujaca jako parametr wskaznik na pierwszy element listy o
# wartosciach typu int, usuwajaca wszystkie elementy, których wartosc dzieli bez reszty wartosc bezposrednio
# nastepujacych po nich elementów.

from Node import Node


# Pomocnicza do testowania
def list_to_node(T) -> Node:
    head = Node()
    p = head
    for v in T:
        temp = Node(v)
        p.next = temp
        p = p.next
    return head.next


def remove(head: Node) -> Node:
    p, q, r = head.next, head, None
    beg = None
    while p:
        # Q dzieli P. bez reszty
        if p.val % q.val == 0:
            # trzeba ujebac poczatek
            if r is None:
                head = head.next
                p, q, r = p.next, p, None
                continue
            # albo i nie
            beg = r if not beg else beg
        else:
            if beg:
                beg.next, beg = r.next, None
        p, q, r = p.next, p, q
    if beg:
        beg.next, beg = r.next, None
    return head


# Odsylaczowa z listy (niebieska)
ListNode = Node(12).fill_with_list([24, 48, 9, 27, 8, 4, 24, 48, 25])
ListNode.print()

# Po usunieciu (zielona)
remove(ListNode).print("green")
