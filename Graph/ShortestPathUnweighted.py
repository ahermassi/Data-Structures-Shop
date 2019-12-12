from collections import deque
from Graph import Graph


def shortest_path(source, dest):
    queue = deque([source])
    visited[source] = True
    parent = [-1] * n
    while queue:
        node = queue.popleft()
        neighbors = g[node]
        for neighbor in neighbors:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
                parent[neighbor] = node
    return reconstruct_path(source, dest, parent)


def reconstruct_path(source, dest, parent):
    """ Reconstruct path going backwards from end node. """
    path = []
    while dest != -1:
        path.append(dest)
        dest = parent[dest]
    path.reverse()  # Reverse the order of the nodes so that the path starts at 'source' node and ends at 'dest' node
    return path if path[0] == source else None  # If 'source' and 'dest' are connected, return the path


if __name__ == '__main__':
    graph = Graph(6, False)
    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(1, 5)
    graph.add_edge(2, 4)
    graph.add_edge(4, 5)
    n = graph.num_vertices
    g = graph.graph
    visited = [False] * n
    print(shortest_path(4, 5))
