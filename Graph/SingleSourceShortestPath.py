from Graph import Graph


def create_graph():
    graph = Graph(8, True)
    graph.add_weighted_edge('A', 'B', 3)
    graph.add_weighted_edge('A', 'C', 6)
    graph.add_weighted_edge('B', 'C', 4)
    graph.add_weighted_edge('B', 'D', 4)
    graph.add_weighted_edge('B', 'E', 11)
    graph.add_weighted_edge('C', 'D', 8)
    graph.add_weighted_edge('C', 'G', 11)
    graph.add_weighted_edge('D', 'E', -4)
    graph.add_weighted_edge('D', 'F', 5)
    graph.add_weighted_edge('D', 'G', 2)
    graph.add_weighted_edge('E', 'H', 9)
    graph.add_weighted_edge('F', 'H', 1)
    graph.add_weighted_edge('G', 'H', 2)
    return graph


def topological_sort():
    for i in range(n):  # Call the recursive helper function to store topological sort starting from all vertices 1 by 1
        vertex = chr(i + ord('A'))  # Convert vertex number to vertex character label (specific to this example)
        if vertex not in visited:
            dfs(vertex)


def dfs(vertex):
    visited.add(vertex)
    neighbors = g[vertex]
    for neighbor in neighbors:  # Recur for all the vertices adjacent to this vertex
        if neighbor[0] not in visited:
            dfs(neighbor[0])
    topological_ordering.append(vertex)


def shortest_path(start_vertex):
    """ Find the shortest path to all nodes starting at 'start_vertex' ."""
    distances = [float('inf')] * n
    distances[ord(start_vertex) - ord('A')] = 0
    for vertex in topological_ordering:
        neighbors = g[vertex]
        vertex_id = ord(vertex) - ord('A')
        for neighbor in neighbors:
            neighbor_id = ord(neighbor[0]) - ord('A')  # 'neighbor' is a tuple (vertex, weight)
            distances[neighbor_id] = min(distances[neighbor_id], distances[vertex_id] + neighbor[1])
            # distances[neighbor_id]: shortest distance from start_vertex to current adjacent node
            # distances[vertex_id]: shortest distance from start_vertex to the node whose adjacents are being explored
            # neighbor[1]: weight of edge vertex --> neighbor
    return distances


if __name__ == '__main__':
    graph = create_graph()
    n = graph.num_vertices
    g = graph.graph  # Adjacency list representing the graph
    visited, topological_ordering = set(), []
    topological_sort()
    topological_ordering.reverse()
    print(topological_ordering)
    distances = shortest_path('A')
    print(distances)
