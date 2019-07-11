from collections import defaultdict


# The implementation uses adjacency list representation of graph For an illustrated procedure, check out this link:
# https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, source):
        visited = [False] * len(self.graph)
        self.dfs_util(source, visited)

    def dfs_util(self, source, visited):
        visited[source] = True
        print(source, end=' ')
        for i in self.graph[source]:
            if not visited[i]:
                self.dfs_util(i, visited)

    def dfs_all(self):
        """ ll the vertices may not be reachable from a given vertex (example Disconnected graph). To do complete DFS
        traversal of such graphs, we must call dfs_util() for every vertex. """
        visited = [False] * len(self.graph)
        for v in self.graph.keys():
            if not visited[v]:
                self.dfs_util(v, visited)


if __name__ == '__main__':
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)
    print('Depth First Traversal starting from vertex 2:', end=' ')
    graph.dfs(2)
    print()
    graph.dfs_all()
