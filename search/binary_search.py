import argparse


def binarysearch(sorted_list, search_func, verbose=True):
    """
    BinarySearch searches sorted_list with search_func,
    which is a function that takes in an element in sorted_list,
    and returns:
        -1  if the item under search is "lesser" than the input element
        +1  if the item under search is "greater" than the input element
         0  if the item under search is equal to the input element

    BinarySearch itself returns the list position of the found element.

    :param sorted_list: list
    :param func: func
    :return: int
    """

    def pprint(*args, **kwargs):
        if verbose:
            print(*args, **kwargs)

    pprint("Binary Search on list of size {}".format(len(sorted_list)))
    if len(sorted_list) == 1:
        return 0

    pos = int(len(sorted_list) / 2)
    r = search_func(sorted_list[pos])

    if r == 0:
        return pos

    if r < 0:
        pprint("searching left!")
        return binarysearch(sorted_list[:pos], search_func, verbose=verbose)

    if r > 0:
        pprint("searching right!")
        return pos + binarysearch(sorted_list[pos:], search_func, verbose=verbose)


def main(args):
    print("item={}".format(args.item))
    print("max={}".format(args.max))

    def bs_func(e):
        if args.item == e:
            return 0

        if args.item < e:
            return -1

        if args.item > e:
            return 1

    eg_list = [i for i in range(0, args.max)]
    print("list = {}".format(eg_list))

    position = binarysearch(eg_list, bs_func)
    print("found element {} at index {}".format(args.item, position))


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='example of binary search')
    argparser.add_argument('--max', type=int, default=1000, help='maximum value in the list to run the example')
    argparser.add_argument('item', type=int, default=5, help='item to search for')
    args = argparser.parse_args()

    main(args)
