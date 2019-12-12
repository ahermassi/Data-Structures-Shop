class Node:
    """ We represent the edges using an array of linked lists. This is the class definition of linked list node. """
    def __init__(self, val):
        self.val = val  # adjacency info, we assign each vertex a unique identification number from 1 to num_vertices
        self.weight = 0  # edge weight, if any
        self.next = None  # next edge in list


class Graph:
    def __init__(self, num_vertices, directed):
        self.num_vertices = num_vertices  # number of vertices in graph
        self.graph = [None] * self.num_vertices  # adjacency info, array of vertices; graph[i] is a linked list
        # representing the adjacent vertices of vertex i
        self.degree = [0] * self.num_vertices  # out-degree of each vertex
        self.directed = directed  # is the graph directed?

    def insert_edge(self, source, dest):
        self.helper(source, dest)
        if not self.directed:
            self.helper(dest, source)

    def helper(self, source, dest):
        node = Node(dest)
        node.next = self.graph[source]  # The new edge is inserted at the head of the appropriate adjacency list, since
        # order doesn't matter
        self.graph[source] = node  # The new edge is now the head of the linked list
        self.degree[source] += 1

    def print_graph(self):
        for i in range(self.num_vertices):  # Printing the associated is just a matter of two nested loops, one through
            # vertices, the other through adjacent edges
            print('Vertex', i)
            adjacent = self.graph[i]  # This is the head of linked list of adjacent vertices
            while adjacent:
                print('Edge ' + str(i) + '->' + str(adjacent.val))
                adjacent = adjacent.next
            print()


if __name__ == '__main__':
    graph = Graph(5, True)
    graph.insert_edge(0, 1)
    graph.insert_edge(0, 4)
    graph.insert_edge(1, 2)
    graph.insert_edge(1, 3)
    graph.insert_edge(1, 4)
    graph.insert_edge(2, 3)
    graph.insert_edge(3, 4)
    graph.print_graph()




