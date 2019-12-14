class GraphWithAdjacencyMatrix:
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


def create_graph():
    graph = GraphWithAdjacencyMatrix(4, True, 'A')
    graph.add_edge('A', 'B', 4)
    graph.add_edge('A', 'C', 1)
    graph.add_edge('A', 'D', 9)
    graph.add_edge('B', 'A', 3)
    graph.add_edge('B', 'C', 6)
    graph.add_edge('B', 'D', 11)
    graph.add_edge('C', 'A', 4)
    graph.add_edge('C', 'B', 1)
    graph.add_edge('C', 'D', 2)
    graph.add_edge('D', 'A', 6)
    graph.add_edge('D', 'B', 5)
    graph.add_edge('D', 'C', -4)
    return graph


def floyd_warshall(adjacency_matrix):
    dp = [[float('infinity')] * n for _ in range(n)]
    for i in range(n):  # Copy adjacency matrix
        for j in range(n):
            dp[i][j] = adjacency_matrix[i][j]
    for k in range(n):  # Compute all pairs shortest paths
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    return dp


if __name__ == '__main__':
    graph = create_graph()
    n = graph.num_vertices
    adjacency_matrix = graph.matrix
    for i in range(n):
        adjacency_matrix[i][i] = 0
    distances = floyd_warshall(adjacency_matrix)
    print(distances)
