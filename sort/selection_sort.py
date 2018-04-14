import argparse
import random


def selectionsort(unsorted_list, compare_func):
    result = []
    while unsorted_list != []:

        pos = 0
        target_value = unsorted_list[0]
        for i, element in enumerate(unsorted_list):
            if compare_func(element, target_value):
                pos = i
                target_value = element

        result.append(unsorted_list.pop(pos))

    return result


def main(args):
    print("max={}".format(args.max))

    def c_func(a, b):
        return a <= b

    eg_list = [i for i in range(0, args.max)]
    random.shuffle(eg_list)
    print("list = {}".format(eg_list))

    result = selectionsort(eg_list, c_func)
    print("sorted : {}".format(result))


if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='example of insertion sort')
    argparser.add_argument('--max', type=int, default=10, help='maximum value in the list to run the example')
    args = argparser.parse_args()

    main(args)
