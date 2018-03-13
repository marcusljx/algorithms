import argparse
import math
from random import shuffle


def quicksort(unsorted_list, compare_func):
    """
    quicksort returns a sorted list from the elements of unsorted_list.
    compare_func is a function that takes in two arguments a and b(where
    a and b are of the same type in unsorted_list) and returns:
        True    if a should be sorted to the left of b
        False   if a should be sorted to the right of b

    The compare_func should be able to handle situations where a==b.

    :param unsorted_list: list
    :param compare_func: func
    :return: list
    """
    if len(unsorted_list) < 2:
        return unsorted_list

    m = unsorted_list[0]
    A, B = [], []
    for x in unsorted_list[1:]:
        if compare_func(x, m):
            A += [x]
        else:
            B += [x]

    return quicksort(A, compare_func) + [m] + quicksort(B, compare_func)


def main(args):
    print("max={}".format(args.max))

    def c_func(a, b):
        return a <= b

    eg_list = [i for i in range(0, args.max)]
    shuffle(eg_list)
    print("list = {}".format(eg_list))

    result = quicksort(eg_list, c_func)
    print("sorted : {}".format(result))


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='example of insertion sort')
    argparser.add_argument('--max', type=int, default=1000, help='maximum value in the list to run the example')
    args = argparser.parse_args()

    main(args)
