from typing import Any, Callable, List
from collections import deque


class BinaryNode:
    def __init__(self, value: Any):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None

    def is_leaf(self):
        if self.left_child or self.right_child:
            return False
        return True

    def add_left_child(self, value: Any):
        self.left_child = BinaryNode(value)
        self.left_child.parent = self

    def add_right_child(self, value: Any):
        self.right_child = BinaryNode(value)
        self.right_child.parent = self

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.left_child.traverse_post_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        if self.left_child is not None:
            self.left_child.traverse_pre_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_pre_order(visit)

    def __str__(self):
        return str(self.value)


class BinaryTree:
    root: BinaryNode

    def __init__(self, root: BinaryNode):
        self.root = root

    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)


def all_paths(tree: BinaryTree) -> List[List[BinaryNode]]:
    root = tree.root
    path = []
    lista = []
    stack = deque()
    stack.append((root, path))
    while stack:
        node, path = stack.pop()
        path.append(node.value)
        if node.right_child:
            stack.append((node.right_child, list(path)))
        if node.left_child:
            stack.append((node.left_child, list(path)))
        if node.is_leaf():
            lista.append(list(path))
    return lista


tree1 = BinaryNode(1)

tree1.add_left_child(2)
tree1.add_right_child(3)

tree1.left_child.add_left_child(4)
tree1.left_child.add_right_child(5)

tree1.right_child.add_right_child(7)

tree1.left_child.left_child.add_left_child(8)
tree1.left_child.left_child.add_right_child(9)

dr = BinaryTree(tree1)
print(all_paths(dr))

assert dr.root.value == 1
assert dr.root.left_child.value == 2
assert dr.root.right_child.is_leaf() is False
assert dr.root.left_child.left_child.left_child.value == 8
assert dr.root.left_child.left_child.left_child.is_leaf() is True
