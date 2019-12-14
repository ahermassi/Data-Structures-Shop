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
    next = [[-1] * n for _ in range(n)]  # Matrix used to reconstruct shortest paths. next[i][j] is the node to go
    # through if we want the shortest distance from i to j
    for i in range(n):  # Copy adjacency matrix
        for j in range(n):
            dp[i][j] = adjacency_matrix[i][j]
            if adjacency_matrix[i][j] != float('infinity'):  # If j is reachable from i, then the next node we want
                # to go to from i is j by default
                next[i][j] = j
    for k in range(n):  # Compute all pairs shortest paths
        for i in range(n):
            for j in range(n):
                if dp[i][k] + dp[k][j] < dp[i][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
                    next[i][j] = next[i][k]
    # Propagate negative cycles.
    # Execute Floyd-Warshall a second time, but this time if the distance can be improved set the optimal distance to
    # -infinity. Every edge (i, j) marked with -infinity is either part of or reaches into a negative cycle.
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] + dp[k][j] < dp[i][j]:
                    dp[i][j] = float('-infinity')
                    next[i][j] = -1  # If we want to go from i to j, we're gonna be trapped into a negative cycle
    return dp, next


def reconstruct_path(start, end):
    path = []
    start, end = ord(start) - ord('A'), ord(end) - ord('A')
    if distances[start][end] == float('infinity'):
        return None
    while start != end:
        if start == -1:  # Reached a negative cycle
            return None
        path.append(start)
        start = next[start][end]
    if next[start][end] == -1:  # Reached a negative cycle
        return None
    path.append(end)
    return path


if __name__ == '__main__':
    graph = create_graph()
    n = graph.num_vertices
    adjacency_matrix = graph.matrix
    for i in range(n):
        adjacency_matrix[i][i] = 0
    distances, next = floyd_warshall(adjacency_matrix)
    print(distances)
    print(reconstruct_path('A', 'C'))
