import random

from bgcolors import *

colors = bcolors()


class LinkedList:
    def __init__(self, val=None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def print(self, color="blue"):
        p = self
        els = []
        while p is not None:
            els.append(colors.bold(str(p.val)))
            p = p.next
        if color == "green":
            print(colors.green(" → ").join(els), end="")
            print(colors.green(" → ") + str(p))
        elif color == "blue":
            print(colors.blue(" → ").join(els), end="")
            print(colors.blue(" → ") + str(p))
        elif color == "yellow":
            print(colors.yellow(" → ").join(els), end="")
            print(colors.yellow(" → ") + str(p))

    def random_fill(self, n):
        p = self
        for i in range(n):
            n = LinkedList()
            n.val = random.randint(p.val + 1, p.val + 5)
            n.prev = p
            p.next, p = n, n
        return n

    def crazy_fill(self, n):
        p = self
        k = p.val
        for i in range(n):
            n = LinkedList()
            n.val = random.randint(k - 20, k + 20)
            n.prev = p
            p.next, p = n, n
        return n

    def fill_with_list(self, T: list):
        p = self
        for v in T:
            temp = LinkedList(v)
            p.next = temp
            temp.prev = p
            p = p.next
        return self
