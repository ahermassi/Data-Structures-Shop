from Graph import Graph


def dfs(source):
    dfs_util(source)


def dfs_util(source):
    if visited[source]:
        return
    visited[source] = True
    print(source, end=' ')
    neighbors = g[source]
    for i in neighbors:
        dfs_util(i)


def dfs_all():
    """ All the vertices may not be reachable from a given vertex (example disconnected graph). To do complete DFS
    traversal of such graphs, we must call dfs_util() for every vertex. """
    for vertex in g:
        if not visited[vertex]:
            dfs_util(vertex)


if __name__ == '__main__':
    graph = Graph(4, False)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)
    n = graph.num_vertices
    g = graph.graph  # Adjacency list representing the graph
    visited = [False] * n
    print('Depth First Traversal starting from vertex 2:', end=' ')
    dfs(2)
