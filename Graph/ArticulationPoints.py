from Graph import Graph


def create_graph():
    graph = Graph(9, False)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(2, 5)
    graph.add_edge(3, 4)
    graph.add_edge(5, 6)
    graph.add_edge(6, 7)
    graph.add_edge(7, 8)
    graph.add_edge(8, 5)
    return graph


def find_articulation_points():
    articulation_points = []
    next_id = 0
    for vertex in range(n):
        if vertex not in visited:
            outcoming_edge_count = 0
            dfs(vertex, vertex, next_id, -1, outcoming_edge_count)
            if outcoming_edge_count > 1:
                articulation_points.append(vertex)
    return articulation_points


def dfs(root, vertex, parent, next_id, outcoming_edge_count):
    if parent == root:
        outcoming_edge_count += 1
    visited.add(vertex)
    ids[vertex] = low_links[vertex] = next_id  # low_links[vertex] is the smallest id of nodes reachable from 'vertex'
    # including 'vertex' itself
    next_id += 1
    neighbors = g[vertex]
    for neighbor in neighbors:
        if neighbor == parent:  # The graph is undirected, so the parent is one of the adjacent vertices
            continue
        if neighbor not in visited:
            dfs(root, neighbor, vertex, next_id, outcoming_edge_count)
            low_links[vertex] = min(low_links[vertex], low_links[neighbor])
            if ids[vertex] <= low_links[neighbor]:  # Verifying the articulation point condition
                articulation_points.append(vertex)
        else:  # Since the current vertex can reach the previously explored adjacent vertex, at this point we can
            # adjust the low link of current vertex if the id of its neighbor is less than the low link of the vertex
            low_links[vertex] = min(low_links[vertex], ids[neighbor])


if __name__ == '__main__':
    graph = create_graph()
    n = graph.num_vertices
    g = graph.graph  # Adjacency list representing the graph
    visited = set()
    ids, low_links = [0] * n, [0] * n
    articulation_points = find_articulation_points()
    print(articulation_points)
