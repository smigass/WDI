# Zadanie 8. Dana jest niepusta lista, proszę napisac funkcje usuwajaca co drugi element listy. Do funkcji
# nalezy przekazac wskazanie na pierwszy element listy.


from Node import Node


# Sytuacja wyglada tak ze q idzie sobie za p (tak na poczatku)
# id: 0  1  2  3  4  5
#     q
#        p
# id: 0  1  2  3  4  5 (head.next -> L [2]), więc podstawienie za L[1].next -> L[3] nic nie zmieni
#        q
#           p
# id: 0  1  2  3  4  5 tutaj jednak L[2].next (q.next) podstawiamy p.next
#           q
#              p


def delete(head: Node):
    p: Node = head.next
    q: Node = head
    while p is not None:
        q.next = p.next
        p, q = p.next, p
    return head


# Tworzenie listy (niebieska)
ListNode = Node(1)
ListNode.random_fill(16)
ListNode.print()

# Usuwanie co drugiego indeksu (zielona)
ListNode = delete(ListNode)
ListNode.print("green")
