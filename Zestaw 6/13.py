# Zadanie 13. Proszę napisac funkcje, otrzymujaca jako parametr wskaznik na pierwszy element listy o
# wartosciach typu int, usuwajaca wszystkie elementy, których wartosc jest mniejsza od wartosci bezposrednio
# poprzedzajacych je elementów.

from Node import Node


def remove(head: Node):
    p, q = head, None
    beg = None
    while p is not None:
        if q and p.val < q.val:
            beg = q if not beg else beg
        else:
            if beg:
                beg.next, beg = q.next, None
        p, q = p.next, p
    return head


ListNode = Node(50)
ListNode.crazy_fill(20)
ListNode.print()

ListNode = remove(ListNode)
ListNode.print("green")
