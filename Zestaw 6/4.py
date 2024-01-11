from Node import Node


def reverse(List):
    h = List
    while List is not None:
        temp = Node(List.val)
        temp.next = h
        h = temp
        List = List.next
    return h


# Tworzenie listy (niebieska)
head = Node(54)
head.random_fill(9)
head.print()

# Odwracanie kolejności (zielona)
k1 = reverse(head)
k1.print("green")
