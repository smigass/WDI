# Zadanie 3. Proszę napisac funkcje scalajaca dwie posortowane listy w jedna posortowana liste. Do funkcji
# nalezy przekazac wskazania na pierwsze elementy obu list, funkcja powinna zwrócic wskazanie do scalonej
# listy. - funkcja iteracyjna, - funkcja rekurencyjna.

# TODO - rekurencyjnie jeszcze

from Node import *


def merge(p1, p2):
    head = Node(0)
    p = head
    while p1 is not None or p2 is not None:
        temp = Node()
        if p1 is None or p2.val < p1.val:
            temp.val = p2.val
            p2 = p2.next
        else:
            temp.val = p1.val
            p1 = p1.next
        p.next = temp
        p = p.next
    return head.next


# Tworzenie pierwszej listy (zielona 1)
head1 = Node(10)
head1.random_fill(10)
head1.print("green")

# Tworzenie drugiej listy (zielona 2)
head2 = Node(30)
head2.random_fill(10)
head2.print("green")

# Łącznie list (niebieska)
j = merge(head1, head2)
j.print()
