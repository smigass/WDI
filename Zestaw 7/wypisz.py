from Node import Node


def print_tree(p: Node):
    if p is not None:
        print(p.val)
        print_tree(p.right)
        print_tree(p.left)


def sum_tree(p):
    if p is None:
        return 0
    return sum_tree(p.left) + sum_tree(p.right) + 1


def tree_h(p: Node) -> int:
    if p is None:
        return 0
    return max(sum_tree(p.left), sum_tree(p.right)) + 1


def count_n(p: Node, n: int) -> int:
    if p is None:
        return 0
