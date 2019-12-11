from GraphAlgorithmDesignManual.Graph import build_graph


visited = set()


def dfs(graph, source):
    visited.add(source)
    print(source)
    adjacent = graph.edges[source]
    while adjacent:
        val = adjacent.val
        if val not in visited:
            dfs(graph, val)
        adjacent = adjacent.next


if __name__ == '__main__':
    graph = build_graph(False)
    dfs(graph, 0)

