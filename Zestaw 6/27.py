# Zadanie 27. Proszę napisac funkcje scalajaca dwie posortowane listy w jedna posortowana liste. Do funkcji
# nalezy przekazac wskazania na pierwsze elementy obu list, funkcja powinna zwrócic wskazanie do scalonej
# listy. - funkcja iteracyjna, - funkcja rekurencyjna.

# To samo co zadanie 3, ale tam mam tylko iteracyjna

from Node import Node


def merge(p1, p2, List=Node(), new=None):
    if new:
        q = List
        while q.next is not None:
            q = q.next
        new.next = None
        q.next = new
    if p1 and p2:
        res = merge(p1.next, p2, List, p1) if p1.val < p2.val else merge(p1, p2.next, List, p2)
        return res
    elif p1:
        return merge(p1.next, p2, List, p1)
    elif p2:
        return merge(p1, p2.next, List, p2)
    else:
        return List.next


List1 = Node(10).random_fill(11)
List2 = Node(9).random_fill(12)
List1.print()
List2.print("green")

merge(List1, List2).print("yellow")
