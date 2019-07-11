class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matrix = [[-1] * self.num_vertices for _ in range(self.num_vertices)]  # vertices x vertices 2D array.
        # matrix[i][j] = 1 indicates that there is an edge from vertex i to vertex j
        self.vertices = {}
        self.vertices_list = [0] * num_vertices  # mapping vertex index to vertex label: ['a', 'b', 'c', 'd', 'e', 'f']

    def set_vertex(self, vertex, vertex_id):
        self.vertices_list[vertex] = vertex_id  # set_vertex(0, 'a') results in vertices_list[0] = 'a'
        self.vertices[vertex_id] = vertex  # set_vertex(0, 'a') results in an entry {'a': 0} in vertices dictionary

    def set_edge(self, frm, to, cost=1):
        frm = self.vertices[frm]  # Get the integer index of the vertex from the dictionary
        to = self.vertices[to]
        self.matrix[frm][to] = cost
        self.matrix[to][frm] = cost  # Adjacency matrix of an undirected graph is symmetric

    def get_vertices(self):
        return self.vertices_list

    def get_edges(self):
        edges = [(self.vertices_list[i], self.vertices_list[j])
                 for i in range(self.num_vertices)
                 for j in range(self.num_vertices)
                 if self.matrix[i][j] != -1]
        return edges

    def get_matrix(self):
        return self.matrix


if __name__ == '__main__':
    graph = Graph(6)

    graph.set_vertex(0, 'a')
    graph.set_vertex(1, 'b')
    graph.set_vertex(2, 'c')
    graph.set_vertex(3, 'd')
    graph.set_vertex(4, 'e')
    graph.set_vertex(5, 'f')

    graph.set_edge('a', 'e', 10)
    graph.set_edge('a', 'c', 20)
    graph.set_edge('c', 'b', 30)
    graph.set_edge('b', 'e', 40)
    graph.set_edge('e', 'd', 50)
    graph.set_edge('f', 'e', 60)

    print("Vertices of the graph: ", graph.get_vertices())
    print("Edges of the graph: ", graph.get_edges())
    print("Adjacency matrix of the graph: ", graph.get_matrix())



