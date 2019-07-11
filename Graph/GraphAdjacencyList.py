class Node:
    def __init__(self, data):
        self.vertex = data
        self.next = None


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [None] * self.vertices  # A graph is the list of the adjacency lists. Size of the list is equal
        # to the number of vertices. list[i] represents the list of vertices adjacent to the ith vertex

    def add_edge(self, src, dest):
        node = Node(dest)
        node.next = self.graph[src]  # Adjacent nodes are like a linked list
        self.graph[src] = node

        # Adding the source node to the destination as it is the undirected graph
        node = Node(src)
        node.next = self.graph[dest]
        self.graph[dest] = node

    def print_graph(self):
        for i in range(self.vertices):
            print('Adjacency list of vertex {}\nhead'.format(i), end=' ')
            adj = self.graph[i]
            while adj:
                print('-> {} '.format(adj.vertex), end='')
                adj = adj.next
            print()


if __name__ == '__main__':
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.print_graph()
