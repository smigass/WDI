# Zadanie 1. Zaimplementuj zbiór mnogosciowy liczb naturalnych korzystajac ze struktury listy odsyłaczowej.
# 1. czy element nalezy do zbioru
# 2. wstawienie elementu do zbioru
# 3. usuniecie elementu ze zbioru

from Node import Node
from bgcolors import bcolors

colors = bcolors()


def member_of(zb, el):
    while zb is not None:
        if zb.val == el:
            return True
        zb = zb.next
    return False


def member_of2(zb, el):
    # dla posortowanego łańcucha
    while zb is not None and zb.val < el:
        zb = zb.val
    return zb is not None and zb.val == el


def insert(zb, el):
    p = zb
    q = None
    while p is not None and p.val < el:
        q, p = p, p.next
    if p is not None and p.val == el:
        return zb
    x = Node(el)
    x.next = p
    if q is not None:
        q.next = x
        return zb
    else:
        return x


def remove(zb, el):
    p = zb
    q = None
    while p is not None and p.val < el:
        p, q = p.next, p
    if p is not None and p.val == el:
        q.next = p.next

    else:
        print(str(colors.fail(f"brak elementu {el}")))


head = Node(10)
tail = head.random_fill(10)
head.print()
print("Czy 27 jest w liscie?: " + str(member_of(head, 27)))
head = insert(head, 76)
head.print("green")
print("Lista po dodaniu 76")
remove(head, 21)
head.print("yellow")
print(f'lista po usunieciu {21}')
