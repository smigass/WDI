# Zadanie 21. Kolejne elementy listy o zwiekszajacej się wartosci pola val nazywamy podlista rosnaca.
# Proszę napisac funkcje, która usuwa z listy wejsciowej najdłuzsza podliste rosnaca. Warunkiem usuniecia
# jest istnienie w liscie dokładnie jednej najdłuzszej podlisty rosnacej.
import math

from Node import Node


def wartownik(List: Node) -> Node:
    new_node = Node(-math.inf)
    new_node.next = List
    return new_node


def remove(head: Node) -> Node:
    head = wartownik(head)
    p, q = head.next, head
    beg, end, curr_beg = head, head, head
    max_length, curr_length = 0, 0
    can_remove = True
    while p:
        if p.val > q.val:
            curr_length += 1
            if curr_length > max_length:
                beg, end = curr_beg, p
        else:
            if curr_length == max_length:
                can_remove = False
            elif curr_length > max_length:
                max_length = curr_length
                can_remove = True
            curr_beg, curr_length = q, 1
        p, q = p.next, p
    if curr_length == max_length:  # Tak, wiem, paskudne, ale nie mam już psychy
        can_remove = False
    elif curr_length > max_length:
        max_length = curr_length
        can_remove = True
    if can_remove:
        beg.next = end.next
    return head.next


# TRZEBA ZMIENIC W Node.py W METODZIE CRAZY FILL RANDOM.RANDINT PRZEDZIAL Z p.val + 1 NA p.val
ListNode = Node(12)
ListNode.crazy_fill(12)
ListNode.print()

ListNode = remove(ListNode)
if ListNode:
    ListNode.print("green")
else:
    print(ListNode)
