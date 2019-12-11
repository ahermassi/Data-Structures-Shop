class Edge:
    """ We represent the edges using an array of linked lists. This is the class definition of linked list node. """
    def __init__(self):
        self.val = 0  # adjacency info, we assign each vertex a unique identification number from 1 to num_vertices
        self.weight = 0  # edge weight, if any
        self.next = None  # next edge in list


class Graph:
    def __init__(self, num_vertices, num_edges, directed):
        self.num_vertices = num_vertices  # number of vertices in graph
        self.num_edges = num_edges  # number of edges in graph
        self.edges = [None] * self.num_vertices  # adjacency info, array of edges; edges[i] is a linked list
        # representing the adjacent vertices of vertex i
        self.degree = [0] * self.num_vertices  # out-degree of each vertex
        self.directed = directed  # is the graph directed?


def build_graph(directed):
    num_vertices = int(input('Number of vertices: '))
    num_edges = int(input('Number of edges: '))
    graph = Graph(num_vertices, num_edges, directed)
    for i in range(num_edges):
        source = int(input('Source: '))
        dest = int(input('Destination: '))
        insert_edge(graph, source, dest, directed)
    return graph


def insert_edge(graph, source, dest, directed):
    edge = Edge()
    edge.val = dest
    edge.next = graph.edges[source]  # The new edge is inserted at the head of the appropriate adjacency list, since
    # order doesn't matter
    graph.edges[source] = edge  # The new edge is now the head of the linked list
    graph.degree[source] += 1
    if not directed:
        insert_edge(graph, dest, source, True)  # We use directed=True to avoid reconstructing the same edge in the
        # next call of insert_edge()
    else:
        graph.num_edges += 1


def print_graph(graph):
    for i in range(graph.num_vertices):  # Printing the associated is just a matter of two nested loops, one through
        # vertices, the other through adjacent edges
        print('Vertex', i)
        adjacent = graph.edges[i]  # This is the head of linked list of adjacent vertices
        while adjacent:
            print('Edge ' + str(i) + '->' + str(adjacent.val))
            adjacent = adjacent.next
        print()


if __name__ == '__main__':
    graph = build_graph(False)
    print_graph(graph)




