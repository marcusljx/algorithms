import argparse
import random


def bubblesort(unsorted_list, compare_func):
    iterations = 0
    for last_pos in range(len(unsorted_list), 0, -1):
        for i in range(0, last_pos-1) :
            j=i+1
            if not compare_func(unsorted_list[i],unsorted_list[j]):
                unsorted_list[i], unsorted_list[j] = unsorted_list[j],  unsorted_list[i]
            iterations += 1

    print("iterations=[{}]".format(iterations))
    return unsorted_list


def main(args):
    print("max={}".format(args.max))

    def c_func(a, b):
        return a <= b

    eg_list = [i for i in range(0, args.max)]
    random.shuffle(eg_list)
    print("list = {}".format(eg_list))

    result = bubblesort(eg_list, c_func)
    print("sorted : {}".format(result))


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='example of insertion sort')
    argparser.add_argument('--max', type=int, default=100, help='maximum value in the list to run the example')
    args = argparser.parse_args()

    main(args)
