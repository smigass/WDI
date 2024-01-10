# Zadanie 19. Elementy w liscie są uporzadkowane według wartosci klucza. Proszę napisac funkcje usuwajaca
# z listy elementy o nieunikalnym kluczu. Do funkcji przekazujemy wskazanie na pierwszy element listy,
# funkcja powinna zwrócic liczbe usunietych elementów.

from Node import Node


def filter(head: Node) -> Node:
    q, p = head, head.next
    beg = None
    while p:
        if q.val == p.val:
            beg = q if beg is None else beg
        elif beg:
            beg.next = p
            beg = None
        p, q = p.next, p
    if beg:
        beg.next = p
    return head


# Lista randomowa o dlugosci 1 + 15 (niebieska)
LinkedList = Node(10)
LinkedList.random_fill(15)
LinkedList.print()

# Lista po filtrowaniu (zielona)
LinkedList = filter(LinkedList)
LinkedList.print("green")
