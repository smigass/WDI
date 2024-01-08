import random

from bgcolors import *

colors = bcolors()


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

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
            n = Node()
            n.val = random.randint(p.val + 1, p.val + 5)
            p.next, p = n, n
        return n