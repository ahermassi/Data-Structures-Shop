class GraphAdjacencyMatrix:
    def __init__(self, num_vertices, directed, base):
        self.num_vertices = num_vertices
        self.base = base  # Base denotes the smallest value of an edge id. This is useful for the matrix indexation
        self.matrix = [[float('infinity')] * self.num_vertices for _ in range(self.num_vertices)] # matrix[i][j] = c
        # indicates that there is an edge from vertex i to vertex j of cost c
        self.directed = directed

    def add_edge(self, u, v, cost=1):
        if isinstance(self.base, int):
            u, v = u - self.base, v - self.base
        elif isinstance(self.base, str):
            u, v = ord(u) - ord(self.base), ord(v) - ord(self.base)
        self.matrix[u][v] = cost
        if not self.directed:
            self.matrix[v][u] = cost  # Adjacency matrix of an undirected graph is symmetric

    def get_matrix(self):
        return self.matrix


if __name__ == '__main__':
    graph = GraphAdjacencyMatrix(6, True, 'a')
    graph.add_edge('a', 'e', 10)
    graph.add_edge('a', 'c', 20)
    graph.add_edge('c', 'b', 30)
    graph.add_edge('b', 'e', 40)
    graph.add_edge('e', 'd', 50)
    graph.add_edge('f', 'e', 60)

    print("Adjacency matrix of the graph: ", graph.get_matrix())



