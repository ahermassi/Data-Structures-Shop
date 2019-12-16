from collections import defaultdict


class Graph:
    def __init__(self, num_vertices, directed):
        self.num_vertices = num_vertices  # number of vertices in graph
        self.graph = defaultdict(list)  # adjacency info, hash map of vertices; graph[i] is a list representing the 
        # adjacent vertices of vertex i
        self.degree = defaultdict(int)  # out-degree of each vertex
        self.directed = directed  # is the graph directed?

    # a -> c
    # b -> c
    # b -> e
    # c -> a
    # c -> b
    # c -> d
    # c -> e
    # d -> c
    # e -> c
    # e -> b

    # The graph can be represented using the following dictionary:
    # graph = { "a" : ["c"],
    #           "b" : ["c", "e"],
    #           "c" : ["a", "b", "d", "e"],
    #           "d" : ["c"],
    #           "e" : ["c", "b"],
    #           "f" : []
    #         }

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.degree[u] += 1
        if not self.directed:
            self.graph[v].append(u)
            self.degree[v] += 1

    def add_weighted_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.degree[u] += 1
        if not self.directed:
            self.graph[v].append((u, w))
            self.degree[v] += 1
            
    def generate_edges(self):
        edges = []
        for vertex, adj_list in self.graph.items():
            for adj in adj_list:
                edges.append((vertex, adj))
        return edges
