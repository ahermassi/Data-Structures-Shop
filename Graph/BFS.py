from collections import deque
from Graph import Graph


def bfs(source):
    """ Traverse vertices reachable from source in a breadth-first manner. """
    queue = deque([source])
    visited[source] = True
    while queue:
        node = queue.popleft()
        print(node, end=' ')
        neighbors = g[source]
        for neighbor in neighbors:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True


if __name__ == '__main__':
    graph = Graph(4, False)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)
    n = graph.num_vertices
    g = graph.graph
    visited = [False] * n
    bfs(2)
