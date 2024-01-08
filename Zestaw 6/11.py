# Zadanie 11. Lista zawiera niepowtarzajace się elementy. Proszę napisac funkcje, do której przekazujemy
# wskaznik na poczatek oraz wartosc klucza. Jezeli element o takim kluczu wystepuje w liscie nalezy go usunac
# z listy. Jezeli elementu o zadanym kluczu brak w liscie nalezy element o takim kluczu wstawic do listy.

from Node import Node


# zakladam, że jest posortowana
def handle(head: Node, key: int) -> Node:
    p = head
    q = None
    if key < p.val:
        return Node(key, head)
    p, q = p.next, p
    while p is not None:
        if p.val == key:
            q.next = p.next
            return head
        if q.val < key < p.val:
            temp = Node(10)
            q.next = temp
            temp.next = p
            return head
        p, q = p.next, p


# Tworzenie listy
ListNode = Node(2)
ListNode.random_fill(12)
ListNode.print()

# Obsługa listy
handle(ListNode, 10).print("green")
