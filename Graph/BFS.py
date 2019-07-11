from collections import defaultdict
# The implementation uses adjacency list representation of graph For an illustrated procedure, check out this link:
# https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, source):
        """ Traverse vertices reachable from source """
        visited = [False] * len(self.graph)  # Mark all the vertices as not visited
        queue = []
        queue.append(source)
        visited[source] = True
        while len(queue) > 0:
            temp = queue.pop(0)
            print(temp, end=' ')
            # Get all adjacent vertices of the dequeued vertex s. If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[temp]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


if __name__ == '__main__':
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)
    graph.bfs(2)