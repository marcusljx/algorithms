class Node:
    def __init__(self, data=None):
        self.data = data
        self.out_edges = []
        self.in_edges = []

    def outgoing_edges(self):
        return self.out_edges

    def incoming_edges(self):
        return self.in_edges

    def edges(self):
        return self.out_edges + self.in_edges

    def link(self, node, incoming=True):
        if incoming:
            edge = (node, self)
            self.in_edges.append(edge)
            node.out_edges.append(edge)
        else:
            edge = (self, node)
            self.out_edges.append(edge)
            node.in_edges.append(edge)

        return edge

    def connects_to(self, node):
        for e in self.edges():
            if e[0] == node or e[1]==node:
                return True

    def __str__(self):
        return 'Node({})'.format(self.data)