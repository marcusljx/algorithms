import argparse

argparser = argparse.ArgumentParser(description='example of binary search')
argparser.add_argument('--max', type=int, default=1000, help='maximum value in the list to run the example')
argparser.add_argument('--verbose', '-v', action="store_true", help='verbose output')
argparser.add_argument('item', type=int, default=5, help='item to search for')
args = argparser.parse_args()


def BinarySearch(sorted_list, search_func):
    """
    BinarySearch searches sorted_list with search_func,
    which is a func that takes in an element in sorted_list,
    and returns:
        -1  if the item under search is "lesser" than the input element
        +1  if the item under search is "greater" than the input element
         0  if the item under search is equal to the input element

    BinarySearch itself returns the list position of the found element.

    :param sorted_list: list
    :param func: func
    :return: int
    """

    v_print("Binary Search on list of size {}".format(len(sorted_list)))
    if len(sorted_list) == 1:
        return 0

    pos = int(len(sorted_list) / 2)
    r = search_func(sorted_list[pos])

    if r == 0:
        return pos

    if r < 0:
        v_print("searching left!")
        return BinarySearch(sorted_list[:pos], search_func)

    if r > 0:
        v_print("searching right!")
        return pos + BinarySearch(sorted_list[pos:], search_func)


def v_print(*p_args, sep=' ', end='\n', file=None):
    if args.verbose:
        print(*p_args, sep=sep, end=end, file=file)


def main():
    v_print("item={}".format(args.item))
    v_print("max={}".format(args.max))

    def bs_func(e):
        if args.item == e:
            return 0

        if args.item < e:
            return -1

        if args.item > e:
            return 1

    eg_list = [i for i in range(0, args.max)]
    v_print("list = {}".format(eg_list))

    position = BinarySearch(eg_list, bs_func)
    print("found element {} at index {}".format(args.item, position))


if __name__ == '__main__':
    main()
