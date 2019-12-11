from collections import deque
from GraphAlgorithmDesignManual.Graph import build_graph


def bfs(graph, source):
    visited, parent = set(), [None] * graph.num_vertices
    queue = deque([source])
    visited.add(source)
    while queue:
        u = queue.popleft()
        print(u)
        adjacent = graph.edges[u]
        while adjacent:
            v = adjacent.val
            if v not in visited:
                visited.add(v)
                parent[v] = u
                queue.append(v)
            adjacent = adjacent.next


if __name__ == '__main__':
    graph = build_graph(False)
    bfs(graph, 0)



