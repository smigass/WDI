from Node import Node


def sort(p):
    if p is None:
        return None
    tails = [None for i in range(10)]
    heads = [None for i in range(10)]
    while p:
        a = p.val % 10
        if tails[a]:
            tails[a].next = p
            tails[a] = p
        else:
            tails[a] = p
            heads[a] = p
        p = p.next
    last = tails[0]
    for i in range(1, 10):
        if heads[i]:
            last.next = heads[i]
            last = tails[i]
    last.next = None
    return heads[0]


head = Node(10)
head.crazy_fill(100)
head.print()

sort(head).print("green")
