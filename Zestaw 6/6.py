# Zadanie 6. Proszę napisac funkcje wstawiajaca na koniec listy nowy element. Do funkcji nalezy przekazac
# wskazanie na pierwszy element listy oraz wstawiana wartosc.

from Node import Node


def append(ListNode: Node, value: int):
    p = ListNode
    while p.next is not None:
        p = p.next
    p.next = Node(value)
    return ListNode


# Tworzenie głowy
head = Node(0)
head.random_fill(14)

# Dodawanie elementu value na koniec listy
head = append(head, 2)

head.print("green")
