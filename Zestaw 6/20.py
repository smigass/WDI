# Zadanie 20. Dana jest lista zawierajaca ciag obustronnie domknietych przedziałów. Krance przedziałów
# okresla uporzadkowana para liczb całkowitych. Proszę napisac stosowne deklaracje oraz funkcje redukujaca
# liczbe elementów listy. Na przykład lista: [15,19] [2,5] [7,11] [8,12] [5,6] [13,17] powinien zostac zredukowany
# do listy: [13,19] [2,6] [7,12]
import math
import random

from Node import Node


def reduce(head: Node, iterator: Node, last_min: Node) -> Node:
    p, q = head, None
    minim = head
    prev_minim = None
    if iterator is None:
        return head
    while p is not None:
        if minim.val[0] > p.val[0] >= last_min.val[0] and p is not last_min:
            minim = p
            prev_minim = q
        p, q = p.next, p
    p, q = head, None
    changed = False
    while p is not None and not changed:
        if minim.val[1] >= p.val[0] >= minim.val[0] and p is not minim:
            changed = True
            p.val = [minim.val[0], max(p.val[1], minim.val[1])]
            if prev_minim:
                prev_minim.next = minim.next
            else:
                head = head.next
        p = p.next
    last_min = minim
    if changed:
        return reduce(head, head, Node([-math.inf, -math.inf]))
    else:
        return reduce(head, iterator.next, last_min)


# Tablice do testowania T2 to losowa lista o dlugosci N
N = 3
T = [[15, 19], [2, 5], [7, 11], [8, 12], [5, 6], [13, 17]]
T1 = [[100, 102], [102, 412], [200, 600], [100, 103], [100, 104]]
T2 = []
for i in range(N):
    a, b = random.randint(1, 100), random.randint(1, 100)
    T2.append([min(a, b), max(a, b)])

# Nowa lista ze zwykłej listy na górze
ListNode = Node()
ListNode.fill_with_list(T)
ListNode = ListNode.next
ListNode.print()

# Lista po złączeniu w przedziały
ListNode = reduce(ListNode, ListNode, Node([-math.inf, -math.inf]))
ListNode.print("green")
