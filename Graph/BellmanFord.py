from Graph import Graph


def create_graph():
    graph = Graph(10, True)
    graph.add_weighted_edge(0, 1, 5)
    graph.add_weighted_edge(1, 2, 20)
    graph.add_weighted_edge(1, 5, 30)
    graph.add_weighted_edge(1, 6, 60)
    graph.add_weighted_edge(2, 3, 10)
    graph.add_weighted_edge(2, 4, 75)
    graph.add_weighted_edge(3, 2, -15)
    graph.add_weighted_edge(4, 9, 100)
    graph.add_weighted_edge(5, 4, 25)
    graph.add_weighted_edge(5, 6, 5)
    graph.add_weighted_edge(5, 8, 50)
    graph.add_weighted_edge(6, 7, -50)
    graph.add_weighted_edge(7, 8, -10)
    return graph


def bellman_ford(start_vertex):
    """ An implementation of the Bellman-Ford algorithm. The algorithm finds the shortest path between a starting node
        and all other nodes in the graph. The algorithm also detects negative cycles. If a node is part of a negative
        cycle then the minimum cost for that node is set to -infinity.
    """
    distances = [float('infinity')] * n
    distances[start_vertex] = 0
    # First step: For each vertex, apply relaxation for all the edges (n-1) times
    for _ in range(n-1):
        for vertex in g:  # Process the vertices in no particular order
            neighbors = g[vertex]
            for node, weight in neighbors:
                distances[node] = min(distances[node], distances[vertex] + weight)
    # Second step: Run algorithm a second time to detect which nodes are part of a negative cycle. A negative cycle has
    # occurred if we can find a better path beyond the optimal solution.
    for _ in range(n-1):
        for vertex in range(n):
            neighbors = g[vertex]
            for node, weight in neighbors:
                if distances[vertex] + weight < distances[node]:
                    distances[node] = float('-infinity')
    return distances


if __name__ == '__main__':
    graph = create_graph()
    n = graph.num_vertices
    g = graph.graph  # Adjacency list representing the graph
    start_vertex = 0
    distances = bellman_ford(start_vertex)
    print(distances)
    for i in range(n):
        print('The cost to get from node {} to {} is {}'.format(start_vertex, i, distances[i]))

