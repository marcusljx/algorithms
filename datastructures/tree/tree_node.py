import random

from datastructures import node


class TreeNode(node.Node):
    def __init__(self):
        super().__init__()
        self.children = []

    def add_child(self, node):
        self.children.append(node)
