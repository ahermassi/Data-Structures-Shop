from Graph import Graph


def create_graph():
    graph = Graph(8, True)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(3, 4)
    graph.add_edge(3, 7)
    graph.add_edge(4, 5)
    graph.add_edge(5, 0)
    graph.add_edge(5, 6)
    graph.add_edge(6, 0)
    graph.add_edge(6, 2)
    graph.add_edge(6, 4)
    graph.add_edge(7, 3)
    graph.add_edge(7, 5)
    return graph


def tarjan():
    scc, next_id, stack = [], 0, []
    for vertex in range(n):
        if vertex not in visited:
            dfs(vertex, next_id, stack, scc)
    return scc


def dfs(vertex, next_id, stack, scc):
    ids[vertex] = low_links[vertex] = next_id
    next_id += 1
    visited.add(vertex)
    stack.append(vertex)
    on_stack.add(vertex)  # We use on_stack set to verify if a node is on the stack in constant time (instead of
    # 'if node in stack' which takes O(N) time)
    neighbors = g[vertex]
    for neighbor in neighbors:
        if neighbor not in visited:
            dfs(neighbor, next_id, stack, scc)
        if neighbor in on_stack:
            low_links[vertex] = min(low_links[vertex], low_links[neighbor])
    if ids[vertex] == low_links[vertex]:  # On recursive callback, if we're at the root node (start of SCC), empty the
        # nodes' stack until back to root
        temp = []
        while stack:
            node = stack.pop()
            temp.append(node)
            low_links[node] = low_links[vertex]
            on_stack.remove(node)
            if node == vertex:
                break
        scc.append(temp)


if __name__ == '__main__':
    graph = create_graph()
    n = graph.num_vertices
    g = graph.graph  # Adjacency list representing the graph
    visited, on_stack = set(), set()
    ids, low_links = [0] * n, [0] * n
    strongly_connected_components = tarjan()
    print(strongly_connected_components)
