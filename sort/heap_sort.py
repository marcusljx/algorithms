import random

from datastructures import heap


def heapsort(unsorted_list, ascending=True):
    h = heap.MaxBinaryHeap()
    for i in unsorted_list:
        h.push(i)

    result = []
    for _ in range(len(unsorted_list)):
        if ascending:
            result.insert(0, h.pop())
        else:
            result.append(h.pop())

    return result


if __name__ == '__main__':
    input = [i for i in range(0, 100, 5)]
    random.shuffle(input)
    print("input={}".format(input))

    print("ascending={}".format(heapsort(input, ascending=True)))
    print("descending={}".format(heapsort(input, ascending=False)))
