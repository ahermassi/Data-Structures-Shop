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


def find_bridges():
    bridges = []
    next_id = 0
    for vertex in range(n):
        if vertex not in visited:
            dfs(vertex, -1, next_id, bridges)
    return bridges


def dfs(vertex, parent, next_id, bridges):
    visited.add(vertex)
    ids[vertex] = low_links[vertex] = next_id  # low_links[vertex] is the smallest id of nodes reachable from 'vertex'
    # including 'vertex' itself
    next_id += 1
    neighbors = g[vertex]
    for neighbor in neighbors:
        if neighbor == parent:  # The graph is undirected, so the parent is one of the adjacent vertices
            continue
        if neighbor not in visited:
            dfs(neighbor, vertex, next_id, bridges)
            low_links[vertex] = min(low_links[vertex], low_links[neighbor])
            if ids[vertex] < low_links[neighbor]:  # Verifying the bridge condition
                bridges.append((vertex, neighbor))
        else:  # Since the current vertex can reach the previously explored adjacent vertex, at this point we can
            # adjust the low link of current vertex if the id of its neighbor is less than the low link of the vertex
            low_links[vertex] = min(low_links[vertex], ids[neighbor])


if __name__ == '__main__':
    graph = create_graph()
    n = graph.num_vertices
    g = graph.graph  # Adjacency list representing the graph
    visited = set()
    ids, low_links = [0] * n, [0] * n
    bridges = find_bridges()
    print(bridges)
