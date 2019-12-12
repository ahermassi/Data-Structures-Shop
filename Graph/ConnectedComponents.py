from Graph import Graph

# Find all the connected components of an undirected graph. If the graph is directed, have a look at Tarjan's
# algorithm to find strongly connected components.


def find_components():
    """ Start a DFS at every node (except if it's already been visited) and mark all reachable nodes as being part of
        the same component.
    """
    for i in range(n):
        global count
        if not visited[i]:
            count += 1
            dfs(i)


def dfs(i):
    visited[i] = True
    neighbors = g[i]
    components[i] = count
    for neighbor in neighbors:
        if not visited[neighbor]:
            dfs(neighbor)


if __name__ == '__main__':
    graph = Graph(18, False)
    graph.add_edge(0, 8)
    graph.add_edge(1, 5)
    graph.add_edge(2, 9)
    graph.add_edge(3, 9)
    graph.add_edge(4, 0)
    graph.add_edge(5, 16)
    graph.add_edge(5, 17)
    graph.add_edge(6, 11)
    graph.add_edge(7, 6)
    graph.add_edge(8, 4)
    graph.add_edge(8, 14)
    graph.add_edge(9, 15)
    graph.add_edge(11, 7)
    graph.add_edge(13, 0)
    graph.add_edge(14, 0)
    graph.add_edge(14, 13)
    graph.add_edge(15, 2)
    graph.add_edge(15, 10)

    n = graph.num_vertices
    g = graph.graph  # Adjacency list representing the graph
    visited = [False] * n
    count = 0
    components = [-1] * n
    find_components()
    print(count)
    print(components)
