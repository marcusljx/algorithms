import argparse
import math
from random import shuffle


def MergeSort(unsorted_list, compare_func):
    """
    MergeSort returns a sorted list from the elements of unsorted_list.
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

    # split list and sort recursively
    split_pos = math.ceil(len(unsorted_list)/2)
    A = MergeSort(unsorted_list[:split_pos], compare_func)
    B = MergeSort(unsorted_list[split_pos:], compare_func)

    # join the sorted halves
    result = []
    while len(A)>0 and len(B)>0:
        if compare_func(A[0], B[0]):
            result += [A[0]]
            A = A[1:]
        else:
            result += [B[0]]
            B = B[1:]

    if len(A)>0:
        return result + A

    if len(B)>0:
        return result + B

    return result

def main(args):
    print("max={}".format(args.max))

    def c_func(a, b):
        return a <= b

    eg_list = [i for i in range(0, args.max)]
    shuffle(eg_list)
    print("list = {}".format(eg_list))

    result = MergeSort(eg_list, c_func)
    print("sorted : {}".format(result))

if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='example of insertion sort')
    argparser.add_argument('--max', type=int, default=1000, help='maximum value in the list to run the example')
    args = argparser.parse_args()

    main(args)
