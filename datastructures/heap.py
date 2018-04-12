import math
import random

_parent = lambda pos: int(math.floor((pos - 1) / 2))
_left = lambda pos: (2 * (pos + 1)) -1
_right = lambda pos: _left(pos) + 1


def swap(list, pos_a, pos_b):
    list[pos_a], list[pos_b] = list[pos_b], list[pos_a]


class BinaryHeap:
    def __init__(self):
        self.list = []

    def __iter__(self):
        return self.list

    def __str__(self):
        return str(self.list)


class MaxBinaryHeap(BinaryHeap):
    def push(self, element):
        self.list.append(element)
        p = len(self.list) - 1
        self._bubble_up(p)

    def _bubble_up(self, i):
        if i > 0 and self.list[i] > self.list[_parent(i)]:
            swap(self.list, i, _parent(i))
            self._bubble_up(_parent(i))

    def pop(self):
        swap(self.list, 0, len(self.list)-1)
        result = self.list.pop()
        self._bubble_down(0)
        return result

    def _bubble_down(self, i):
        target = i

        if _left(i) < len(self.list) and self.list[_left(i)] > self.list[target]:
            target = _left(i)

        if _right(i) < len(self.list) and self.list[_right(i)] > self.list[target]:
            target = _right(i)

        # print("current = {}".format( self.list))
        # print("i=[{}]\ttarget=[{}]".format(i, target))
        if target != i:
            swap(self.list, i, target)
            self._bubble_down(target)


if __name__ == '__main__':
    bh = MaxBinaryHeap()
    for _ in range(12):
        bh.push(random.randint(0, 100))
        print(bh)

    for _ in range(12):
        print(bh.pop())
