# Zadanie 26. Proszę napisac funkcje, która sprawdza, czy jedna lista zawiera się w drugiej. Do funkcji nalezy
# przekazac wskazania na pierwsze elementy obu list, funkcja powinna zwrócic wartosc logiczna.

from Node import Node


def check(p1: Node, p2: Node):
    q1, q2 = p1, p2
    while q1 or q2:
        if q1 is p2 or q2 is p1:
            return True
        q1 = q1.next if q1 else q1
        q2 = q2.next if q2 else q2
    return False


ListNode = Node(1).random_fill(10)
ListNode.print()

List2 = Node(10)
List2.next = Node(15)
List2.next.next = ListNode
List2.print_cycle("green")

print(check(List2, ListNode))