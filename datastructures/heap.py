import math
import random

_parent = lambda pos: int(math.floor((pos - 1) / 2))
_left = lambda pos: 2 * pos
_right = lambda pos: 2 * pos + 1


class BinaryHeap:
    def __init__(self, max_heap=True):
        self.is_max_heap = max_heap
        if max_heap:
            self.compare_parent_func = lambda pos: self.list[pos] > self.list[_parent(pos)]
        else:
            self.compare_parent_func = lambda pos: self.list[pos] < self.list[_parent(pos)]

        self.list = []

    def __iter__(self):
        return self.list

    def __str__(self):
        return str(self.list)

    def push(self, element):
        self.list.append(element)
        p = len(self.list)-1
        while self.compare_parent_func(p):
            self.list[p], self.list[_parent(p)] = self.list[_parent(p)], self.list[p]
            p = _parent(p)

    def pop(self):
        root = self.list.pop(index=0)
        self._heapify()
        return root

    def _heapify(self, i=0):
        left = _left(i)
        right = _right(i)
        target = i

        if left <= len(self.list) and self.compare_parent_func(left):
            target = left

        if right <= len(self.list) and self.compare_parent_func(right):
            target = right

        if target != i:
            self.list[i], self.list[target] = self.list[target], self.list[i]
            self._heapify(target)


if __name__ == '__main__':
    bh = BinaryHeap()
    for _ in range(12):
        bh.push(random.randint(0,100))
        print(bh)
