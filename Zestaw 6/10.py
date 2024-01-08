# Zadanie 10. Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę napisac funkcje dodajaca
# dwie takie liczby. W wyniku dodawania dwóch liczb powinna powstac nowa lista.

from Node import Node


# Odwracanie kolejności listy (w sumie też w celach testow do funkcji ponizej)
def reverse(List) -> Node:
    h = None
    while List is not None:
        temp = Node(List.val)
        temp.next = h
        h = temp
        List = List.next
    return h


# Liczba do listy (tak w celach testów)
def to_list(n: int) -> Node:
    head: Node = Node()
    p: Node = head
    while n != 0:
        k = n % 10
        temp = Node(k)
        n //= 10
        p.next = temp
        p = p.next
    return reverse(head.next)


def add(head1: Node, head2: Node) -> Node:
    List: Node = Node()
    q = List
    while head1 or head2:
        temp = Node(0)
        p1, p2 = head1, head2
        q1, q2 = None, None
        if p1: # to samo co p1 is not None
            while p1.next is not None:
                p1, q1 = p1.next, p1
            temp.val += p1.val
        if p2:
            while p2.next is not None:
                p2, q2 = p2.next, p2
            temp.val += p2.val
        if q1 is not None:
            q1.next = None
        else:
            head1 = None
        if q2 is not None:
            q2.next = None
        else:
            head2 = None
        q.next = temp
        q = q.next

    return check_and_fix(reverse(List.next))


def check_and_fix(head: Node) -> Node:
    p: Node = head
    q: Node | None = None
    while p is not None:
        if p.val >= 10:
            k = p.val // 10
            p.val %= 10
            # jeżeli znalazło 10 lub wiecej na pierwszym indeksie to zwracamy nową Liste z dodatkowym Nodem na początku
            if q is None:
                temp = Node(k)
                temp.next = head
                return check_and_fix(temp)
            # jeżeli znalazło 10 lub wiecej w środku listy, to odejmujemy 10 i poprzedni zwiekszamy o val - 9
            # Wywołujemy ta funkcje rekurencyjnie jeszcze raz
            else:
                q.val += k
                return check_and_fix(head)
        p, q = p.next, p
    return head


# Początkowa liczba NATURALNA (zolta)
number1 = to_list(713)
number1.print("yellow")
number2 = to_list(299)
number2.print("yellow")
# Wynik dodawania (zielona)
add(number1, number2).print("green")
