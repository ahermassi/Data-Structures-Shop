from Graph import Graph


def create_graph():
    graph = Graph(13, True)
    graph.add_edge('A', 'D')
    graph.add_edge('B', 'D')
    graph.add_edge('C', 'A')
    graph.add_edge('C', 'B')
    graph.add_edge('D', 'G')
    graph.add_edge('D', 'H')
    graph.add_edge('E', 'A')
    graph.add_edge('E', 'D')
    graph.add_edge('E', 'F')
    graph.add_edge('F', 'J')
    graph.add_edge('F', 'K')
    graph.add_edge('G', 'I')
    graph.add_edge('H', 'I')
    graph.add_edge('H', 'J')
    graph.add_edge('I', 'L')
    graph.add_edge('J', 'L')
    graph.add_edge('J', 'M')
    graph.add_edge('K', 'J')
    return graph


def topological_sort(vertex):
    visited.add(vertex)
    neighbors = g[vertex]
    for neighbor in neighbors:  # Recur for all the vertices adjacent to this vertex
        if neighbor not in visited:
            topological_sort(neighbor)
    topological_ordering.append(vertex)


if __name__ == '__main__':
    graph = create_graph()
    n = graph.num_vertices
    g = graph.graph  # Adjacency list representing the graph
    visited = set()
    topological_ordering = []
    for i in range(n):  # Call the recursive helper function to store topological sort starting from all vertices 1 by 1
        vertex = chr(i + ord('A'))  # Convert vertex number to vertex character label (specific to this example)
        if vertex not in visited:
            topological_sort(vertex)
    topological_ordering = topological_ordering[::-1]
    print(topological_ordering)
