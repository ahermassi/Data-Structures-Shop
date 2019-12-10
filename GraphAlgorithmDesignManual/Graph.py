class Edge:
    """ We represent the edges using an array of linked lists. This is the class definition of linked list node. """
    def __init__(self):
        self.val = 0  # adjacency info, we assign each vertex a unique identification number from 1 to num_vertices
        self.weight = 0  # edge weight, if any
        self.next = None  # next edge in list


class Graph:
    def __init__(self):
        self.edges = []  # adjacency info, array of edges; edges[i] is a linked list representing the adjacent edges
        # of vertex i
        self.degree = []  # out-degree of each vertex
        self.num_vertices = 0  # number of vertices in graph
        self.num_edges = 0  # number of edges in graph
        self.directed = False  # is the graph directed?


