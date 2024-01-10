import random

from bgcolors import *

colors = bcolors()


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

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
            n.val = random.randint(p.val, p.val + 5)
            p.next, p = n, n
        return n

    def crazy_fill(self, n):
        p = self
        k = p.val
        for i in range(n):
            n = Node()
            n.val = random.randint(k - 20, k + 20)
            p.next, p = n, n
        return n

    def fill_with_list(self, T: list):
        p = self
        for v in T:
            temp = Node(v)
            p.next = temp
            p = p.next
        return self

    def fill_with_cycle(self, s, k):
        p = self
        for i in range(s - 1):
            n = Node(random.randint(10, 100))
            p.next = n
            p = p.next
        if k == 0:
            return self
        start = Node(random.randint(10, 100))
        p.next = start
        p = start
        if k == 1:
            start.next = start
            return self
        for i in range(k - 2):
            n = Node(random.randint(10, 100))
            p.next = n
            p = p.next
        n = Node(random.randint(10, 100))
        n.next = start
        p.next = n
        return self.next

    def print_cycle(self, color="blue"):
        s = set()
        slow = self
        while slow not in s:
            s.add(slow)
            slow = slow.next
            if slow is None:
                print(slow)
                self.print(color)
                return 0
        print(slow)
        p = self
        els = []
        while p is not slow:
            els.append(colors.bold(str(p.val)))
            p = p.next
        rest = []
        k = slow.next
        while k is not slow:
            rest.append(colors.fail(colors.bold(str(k.val))))
            k = k.next
        if color == "green":
            print(colors.green(" → ").join(els), end="")
            print(colors.green(" → "), end="")
            print(colors.fail(colors.bold(str(slow.val))), end="")
            print(colors.green(" → "), end="")
            print(colors.green(" → ").join(rest))
        elif color == "blue":
            print(colors.blue(" → ").join(els), end="")
            print(colors.blue(" → "), end="")
            print(colors.fail(colors.bold(str(slow.val))), end="")
            print(colors.blue(" → "), end="")
            print(colors.blue(" → ").join(rest))
        elif color == "yellow":
            print(colors.yellow(" → ").join(els), end="")
            print(colors.yellow(" → "), end="")
            print(colors.fail(colors.bold(str(slow.val))), end="")
            print(colors.yellow(" → "), end="")
            print(colors.yellow(" → ").join(rest))
