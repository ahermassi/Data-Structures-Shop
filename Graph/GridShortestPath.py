from collections import deque


def find_path(source, dest):
    i, j = source
    queue = deque([(i, j, 0)])
    parent = [[-1 for _ in range(7)] for _ in range(5)]  # Keep track of previously visited node (parent) for each node
    while queue:
        x, y, count = queue.popleft()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for d1, d2 in directions:
            xx, yy = x + d1, y + d2
            if 0 <= xx < n and 0 <= yy < m and (xx, yy) not in visited and grid[xx][yy] == '.':
                visited.add((xx, yy))
                queue.append((xx, yy, count + 1))
                parent[xx][yy] = (x, y)

    return reconstruct_path(source, dest, parent)


def reconstruct_path(source, dest, parent):
    """ Reconstruct path going backwards from end node. """
    path = []
    while dest != -1:
        path.append(dest)
        dest = parent[dest[0]][dest[1]]
    path.reverse()  # Reverse the order of the nodes so that the path starts at 'source' node and ends at 'dest' node
    return path if path[0] == source else None  # If 'source' and 'dest' are connected, return the path


if __name__ == '__main__':
    grid = [['' for _ in range(7)] for _ in range(5)]
    grid[0] = ['S', '.', '.', '#', '.', '.', '.']
    grid[1] = ['.', '#', '.', '.', '.', '#', '.']
    grid[2] = ['.', '#', '.', '.', '.', '.', '.']
    grid[3] = ['.', '.', '#', '#', '.', '.', '.']
    grid[4] = ['#', '.', '#', 'E', '.', '#', '.']
    n, m = len(grid), len(grid[0])
    visited = {(0, 0)}
    source, dest = (0, 0), (4, 3)
    print(find_path(source, dest))
