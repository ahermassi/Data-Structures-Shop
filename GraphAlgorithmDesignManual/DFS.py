from GraphAlgorithmDesignManual.Graph import build_graph


visited = set()
processed = set()


def dfs(graph, source):
    visited.add(source)
    # process_vertex_early(source)
    adjacent = graph.edges[source]
    while adjacent:
        val = adjacent.val
        if val not in visited:
            # process_edge(source, val)
            dfs(graph, val)
        elif val not in processed:
            pass
            # process_edge(source, val)
        adjacent = adjacent.next
    # process_vertex_late(source)
    processed.add(source)


if __name__ == '__main__':
    graph = build_graph(False)
    dfs(graph, 0)

