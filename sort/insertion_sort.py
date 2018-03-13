import argparse
from random import shuffle

from search import binary_search


def InsertionSort(unsorted_list, compare_func):
    """
    InsertionSort returns a sorted list from the elements of unsorted_list.
    compare_func is a function that takes in two arguments a and b(where
    a and b are of the same type in unsorted_list) and returns:
        True    if a should be sorted to the left of b
        False   if a should be sorted to the right of b

    The compare_func should be able to handle situations where a==b.

    :param unsorted_list: list
    :param compare_func: func
    :return: list
    """
    result = [unsorted_list[0]]
    print(result)
    for item in unsorted_list[1:]:
        pos = binary_search.BinarySearch(result, lambda e: -1 if compare_func(item, e) else 1, verbose=False)
        if compare_func(item,result[pos]):
            result = result[:pos] + [item] + result[pos:]
        else:
            result = result[:pos+1] + [item] + result[pos+1:]
        print(result)

    return result


def main(args):
    print("max={}".format(args.max))
    def c_func(a, b):
        return a <= b

    eg_list = [i for i in range(0, args.max)]
    shuffle(eg_list)
    print("list = {}".format(eg_list))

    result = InsertionSort(eg_list, c_func)
    print("sorted : {}".format(result))


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='example of insertion sort')
    argparser.add_argument('--max', type=int, default=1000, help='maximum value in the list to run the example')
    args = argparser.parse_args()

    main(args)
