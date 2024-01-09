# Zadanie 15. Proszę napisac funkcje, która otrzymujac jako parametr wskazujacy na poczatek listy jednokierunkowej,
# usuwa z niej wszystkie elementy, w których wartosc klucza w zapisie trójkowym ma wieksza
# ilosc jedynek niż dwójek.

from Node import Node


# Zamiana liczby na system trójkowy do testowania (do zielonej listy)
def to_ternary(n):
    t = 0
    i = 0
    while n != 0:
        t += (n % 3) * 10 ** i
        i += 1
        n //= 3
    return t


# Sprawdzanie, czy liczba spelnia warunki usuniecia
def ternary(number: int) -> bool:
    tab = [0 for i in range(3)]
    while number != 0:
        k = number % 3
        tab[k] += 1
        number //= 3
    return tab[1] > tab[2]


def remove(head: Node) -> Node:
    p, q = head, None
    beg = None
    while p is not None:
        if p == q:  # p i q moga na siebie najsc po usunieciu wiec przesuwamy p
            p = p.next
        elif ternary(p.val):
            if q is None:  # jezeli liczba do usuniecia jest na poczatku to odcinamy pierwszy element i jazda dalej
                head = head.next
                p, q = head, None
                continue
            else:  # jezeli nie to albo zostawiamy beg jezeli jest a jak go nie ma to ustawiamy go na element przed p
                beg = q if not beg else beg
        else:  # jezeli p nie jest ta liczba to jezeli jest beg to usuwamy wszystkie elementu ktore obejmowal (beg, q]
            if beg:
                beg.next, beg = q.next, None
        p, q = p.next, p
    return head


# Odsylaczowa z listy
T = [100, 123, 1421, 23, 13, 1, 14, 23, 15, 21]
ListNode = Node(1).fill_with_list(T)
ListNode.print()

# Pogladowa odsyłaczowa z zamienionymi elementami na system trójkowy
copy = Node(1).fill_with_list([to_ternary(T[i]) for i in range(len(T))])
copy.print("green")

# Po usunięciu elementów
remove(ListNode).print("yellow")
