from Graph import Graph
from heapq import heappush, heappop


def create_graph():
    graph = Graph(5, True)
    graph.add_weighted_edge(0, 1, 4)
    graph.add_weighted_edge(0, 2, 1)
    graph.add_weighted_edge(1, 3, 1)
    graph.add_weighted_edge(2, 1, 2)
    graph.add_weighted_edge(2, 3, 5)
    graph.add_weighted_edge(3, 4, 3)
    return graph


def dijkstra(start_vertex):
    """ Find all the shortest path distances from the start node to every other node. """
    distances = [float('inf')] * n
    visited = set()
    heap = []
    distances[start_vertex] = 0
    heappush(heap, (start_vertex, 0))
    while heap:
        node, d = heappop(heap)
        visited.add(node)
        neighbors = g[node]
        for neighbor in neighbors:
            if neighbor not in visited:  # If the node has been visited, there is no advantage in re-visiting it
                # because its shortest distance will not change as Dijsktra's algorithm processes each next most
                # promising node in order
                distances[neighbor[0]] = min(distances[neighbor[0]], d + neighbor[1])
                heappush(heap, (neighbor[0], distances[neighbor[0]]))
    return distances


def dijkstra_with_path(start_vertex, end_vertex):
    """ Find all the shortest path distances from the start node to every other node while keeping track of the path."""
    distances = [float('inf')] * n
    parent = [None] * n
    visited = set()
    heap = []
    distances[start_vertex] = 0
    heappush(heap, (start_vertex, 0))
    while heap:
        node, d = heappop(heap)
        visited.add(node)
        neighbors = g[node]
        for neighbor in neighbors:
            if neighbor not in visited:
                distances[neighbor[0]] = min(distances[neighbor[0]], d + neighbor[1])
                parent[neighbor[0]] = node
                heappush(heap, (neighbor[0], distances[neighbor[0]]))
    return reconstruct_path(distances, parent, start_vertex, end_vertex)


def reconstruct_path(distances, parent, start_vertex, end_vertex):
    if distances[end_vertex] == float('inf'):
        return None
    path = []
    while end_vertex:
        path.append(end_vertex)
        end_vertex = parent[end_vertex]
    path.reverse()
    return [start_vertex] + path


def dijkstra_shortest_distance(start_vertex, end_vertex):
    """ Dijkstra with early termination. Once we encounter the target node, we return its shortest distance from the
        source.
    """
    distances = [float('inf')] * n
    visited = set()
    heap = []
    distances[start_vertex] = 0
    heappush(heap, (start_vertex, 0))
    while heap:
        node, d = heappop(heap)
        if node == end_vertex:
            return distances[end_vertex]
        visited.add(node)
        neighbors = g[node]
        for neighbor in neighbors:
            if neighbor not in visited:
                distances[neighbor[0]] = min(distances[neighbor[0]], d + neighbor[1])
                heappush(heap, (neighbor[0], distances[neighbor[0]]))


if __name__ == '__main__':
    graph = create_graph()
    n = graph.num_vertices
    g = graph.graph  # Adjacency list representing the graph
    distances = dijkstra(0)
    print(distances)
    path = dijkstra_with_path(0, 4)
    print(path)
    d = dijkstra_shortest_distance(0, 3)
    print(d)
