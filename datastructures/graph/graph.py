import random

from collections import namedtuple

from datastructures.graph import node

linking_iterations = 20

def random_graph(size):
    nodes = [node.Node(data=i) for i in range(size)]

    random_group = lambda g,p : [random.choice(g) for _ in range(int(size * p))]

    edges = []

    for _ in range(linking_iterations):
        r1 = random_group(nodes, 0.1)
        r2 = random_group(nodes, 0.15)

        for n in r1:
            edges += [n.link(target) for target in random_group(r2, 0.4) if n != target and not n.connects_to(target)]

    g = namedtuple("Graph", "V E")
    g.E = edges
    g.V = nodes
    return g
