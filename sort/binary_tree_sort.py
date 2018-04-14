import argparse
import random

from datastructures.tree import binary_search_tree as bst

def binarytreesort(unsorted_list, ascending=True):
    bt = bst.Node(unsorted_list[0])
    for v in unsorted_list[1:]:
        bt.add(bst.Node(v))

    if ascending:
        return [x for x in bt.traverse(left_to_right=True)]
    else:
        return [x for x in bt.traverse(left_to_right=False)]


def main(args):
    print("max={}".format(args.max))

    eg_list = [i for i in range(0, args.max)]
    random.shuffle(eg_list)
    print("list = {}".format(eg_list))

    result = binarytreesort(eg_list, ascending=True)
    print("sorted : {}".format([r.value for r in result]))


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='example of insertion sort')
    argparser.add_argument('--max', type=int, default=10, help='maximum value in the list to run the example')
    args = argparser.parse_args()

    main(args)
