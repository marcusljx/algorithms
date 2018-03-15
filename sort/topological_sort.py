import argparse
from datastructures.graph import graph

def topsort(graph):
    """
    topsort performs topological sort on the graph.

    :param graph: (V, E) where V is a set of Node, E is a set of (Node,Node) tuples
    :return: list of Node
    """
    while len(graph.V) > 0:
        cycle = True
        for node in graph.V:
            if edgeset_contains(graph.E, node, incoming=False):
                graph.V.remove(node)
            for e in graph.E:
                if e[0]== node:
                    graph.E.remove(e)
                    yield node
                    cycle = False

        if cycle:
            raise Exception('cyclic path detected, topological sort is impossible.')



def edgeset_contains(edgeset, node, incoming=True):
    pos=0
    if incoming:
        pos=1

    for e in edgeset:
        if e[pos] == node:
            return True

    return False


def main(args):
    g = graph.random_graph(args.nodes)
    print("=== nodes:")
    for n in g.V:
        print(n)

    print("=== edges:")
    for e in g.E:
        print('({} -> {}'.format(e[0], e[1]))

    print("=== TOPOLOGICAL SORT:")
    for node in topsort(g):
        print(node)



if __name__ == '__main__':
    argparser = argparse.ArgumentParser(description='randomly generate a connected graph and perform topological sort')
    argparser.add_argument('--nodes', default=10, type=int, help='number of nodes to generate a random graph')
    args = argparser.parse_args()
    main(args)