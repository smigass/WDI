# Zadanie 5. Proszę napisac funkcje, która rozdziela elementy listy odsyłaczowej do 10 list, według ostatniej
# cyfry pola val. W drugim kroku powstałe listy nalezy połaczyc w jedna liste odsyłaczowa, która jest
# posortowana niemalejaco według ostatniej cyfry pola val.

# Zrobione nawet trudniej, bo odsyla do odsylaczowych, a nie zwyklych a chyba o to chodziło autorowi.


from Node import Node


def insert(list, el: int):
    p = list
    q = None
    while p is not None and p.val < el:
        p, q = p.next, p
    if p is not None and p.val == el:
        return list
    temp = Node(el)
    temp.next = p
    if q is not None:
        q.next = temp
        return list
    else:
        return temp


def assign(list):
    lists = [None for i in range(10)]
    while list is not None:
        lists[list.val % 10] = insert(lists[list.val % 10], list.val)
        list = list.next
    return lists


def join(lists):
    h = Node()
    p = h
    for L in lists:
        while L is not None:
            temp = Node()
            temp.val = L.val
            p.next = temp
            p = p.next
            L = L.next
    return h.next


# Tworzenie głowy (niebieska)
head = Node(10)
head.crazy_fill(100)
head.print()

# Dzielenie na 1- list odsyłaczowych (zolte)
tab = assign(head)

for v in tab:
    if v is not None:
        v.print("yellow")

# Łączenie 10 list odsyłaczowych w jedną (zielona)
head = join(tab)
head.print("green")
