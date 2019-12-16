from Graph import Graph
from heapq import heappush, heappop


def create_graph():
    graph = Graph(8, False)
    graph.add_weighted_edge(0, 1, 10)
    graph.add_weighted_edge(0, 2, 1)
    graph.add_weighted_edge(0, 3, 4)
    graph.add_weighted_edge(1, 2, 3)
    graph.add_weighted_edge(1, 4, 0)
    graph.add_weighted_edge(2, 3, 2)
    graph.add_weighted_edge(2, 5, 8)
    graph.add_weighted_edge(3, 5, 2)
    graph.add_weighted_edge(3, 6, 7)
    graph.add_weighted_edge(4, 5, 1)
    graph.add_weighted_edge(4, 7, 8)
    graph.add_weighted_edge(5, 6, 6)
    graph.add_weighted_edge(5, 7, 9)
    graph.add_weighted_edge(6, 7, 12)
    return graph


def prim(start_vertex):
    """ This is the eager implementation of Prim's using min heap. """
    mst, heap, cost = [], [], 0
    add_edges(start_vertex, heap)  # Add initial set of edges to the heap starting at start_vertex
    while heap and len(mst) < (n - 1):
        weight, source, dest = heappop(heap)  # Choose the next best vertex to explore
        if dest in visited:  # Skip edges that point to visited nodes (stale edges)
            continue
        cost += weight
        mst.append((source, dest, weight))  # The edge 'source -> dest' is part of the MST since it contributes with
        # the smallest weight (don't forget that the heap is a min heap) and 'dest' vertex was not previously visited
        add_edges(dest, heap)  # 'dest' is the NEXT vertex to explore, so add its edges to the heap
    return mst, cost if len(mst) == n - 1 else (None, None)


def add_edges(vertex, heap):
    visited.add(vertex)
    neighbors = g[vertex]
    for neighbor in neighbors:
        dest, weight = neighbor
        if dest not in visited:  # Only add edges that point to unvisited nodes
            heappush(heap, (weight, vertex, dest))  # Even if this edge exists on the heap, the same edge with a lower
            # cost will replace the old one


if __name__ == '__main__':
    graph = create_graph()
    n = graph.num_vertices
    g = graph.graph  # Adjacency list representing the
    visited = set()
    minimum_spanning_tree, cost = prim(0)
    print('MST cost: {}'.format(cost))
    for source, dest, weight in minimum_spanning_tree:
        print('from: {}, to: {}, cost: {}'.format(source, dest, weight))

