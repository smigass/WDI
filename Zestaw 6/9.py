# Zadanie 9. Dana jest niepusta lista reprezentujaca liczbe naturalna. Kolejne elementy listy przechowuja
# kolejne cyfry. Proszę napisac funkcje zwiekszajaca taka liczbe o 1.

from Node import Node


# Odwracanie kolejności listy (w sumie też w celach testow do funkcji ponizej)
def reverse(List):
    h = None
    while List is not None:
        temp = Node(List.val)
        temp.next = h
        h = temp
        List = List.next
    return h


# Liczba do listy (tak w celach testów)
def to_list(n: int):
    head = Node()
    p = head
    while n != 0:
        k = n % 10
        temp = Node(k)
        n //= 10
        p.next = temp
        p = p.next
    return reverse(head.next)


# zwiekszanie ostatniego indeksu o 1
def increase(head: Node):
    p: Node = head
    q: Node | None = None
    while p is not None:
        p, q = p.next, p
    q.val += 1
    # sprawdzenie, czy przypadkiem nie ma 10
    return check_and_fix(head)


def check_and_fix(head: Node):
    p: Node = head
    q: Node | None = None
    while p is not None:
        if p.val == 10:
            p.val = 0
            # jeżeli znalazło 10 na pierwszym indeksie to zwracamy nową Liste z dodatkowym Nodem na początku
            if q is None:
                temp = Node(1)
                temp.next = head
                return temp
            # jeżeli znalazło 10 w środku listy, to zerujemy indeks i poprzedni zwiekszamy o 1
            # Wywołujemy ta funkcje rekurencyjnie jeszcze raz
            else:
                q.val += 1
                return check_and_fix(head)
        p, q = p.next, p
    return head


# Początkowa liczba NATURALNA (zolta)
number_list = to_list(102)
number_list.print("yellow")

# zwiekszona (zielona)
number_list = increase(number_list)
number_list.print("green")
