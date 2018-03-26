import random
from time import time


class Node(object):
    def __init__(self, value):
        self.value = value
        self.isInsertLeft = lambda node: self.value <= node.value
        self.L = None
        self.R = None

    def set_func(self, left_func):
        self.isInsertLeft = left_func

    def add(self, node):
        if type(node) is not type(self):
            raise Exception("expected node of type {} but received {}".format(type(self), type(node)))

        if self.isInsertLeft(node):
            if self.R is None:
                self.R = node
                print("adding [{}] to the right of [{}]".format(node, self))
            else:
                self.R.add(node)

        else:
            if self.L is None:
                self.L = node
                print("adding [{}] to the left of [{}]".format(node, self))
            else:
                self.L.add(node)

    def traverse(self, left_to_right=True):
        sideOrder = [self.L, self.R] if left_to_right else [self.R, self.L]

        if sideOrder[0] is not None:
            yield from sideOrder[0].traverse(left_to_right)

        yield self

        if sideOrder[1] is not None:
            yield from sideOrder[1].traverse(left_to_right)

    def __str__(self):
        return '{}'.format(self.value)


if __name__ == '__main__':
    max = 100

    rng = random.Random(time())
    N = Node(rng.randint(0, max))

    for i in range(10):
        N.add(Node(rng.randint(0, max)))

    print("=======================================")
    for val in N.traverse():
        print(val)
