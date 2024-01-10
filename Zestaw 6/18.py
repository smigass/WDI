# Zadanie 18. Proszę napisac funkcje, która pozostawia w liscie wyłacznie elementy unikalne. Do funkcji
# nalezy przekazac wskazanie na pierwszy element listy.
import math

from Node import Node


# Funkcja tworzy nowa liste i dla kazdego elementu z poczatkowej sprawdza, czy w nowej tablicy już jest ten element
def filter(head: Node) -> Node:
    p = head
    new = Node(math.inf)
    tail = new
    while p:
        flag = False
        r = new
        while r:
            if r.val == p.val:
                flag = True
            r = r.next
        if not flag:
            tail.next = Node(p.val)
            tail = tail.next
        p = p.next
    return new.next


LinkedList = Node(10)
LinkedList.crazy_fill(15)
LinkedList.print()

LinkedList = filter(LinkedList)
LinkedList.print("green")
