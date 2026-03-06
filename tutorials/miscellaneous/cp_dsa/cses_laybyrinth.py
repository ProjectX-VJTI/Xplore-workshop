def main():
    # CSES Labyrinth problem: https://cses.fi/problemset/task/1193
    n, m = map(int, input().split())
    grid = [input().strip() for _ in range(n)]

    from collections import deque
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * m for _ in range(n)]
    parent = [[None] * m for _ in range(n)] 

    # Find start and end positions
    start = end = None
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'A':
                start = (i, j)
            elif grid[i][j] == 'B':
                end = (i, j)   
    
    # BFS to find shortest path
    queue = deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            break

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] != '#':
                visited[nx][ny] = True
                parent[nx][ny] = (x, y)
                queue.append((nx, ny))

    # Reconstruct path
    if not visited[end[0]][end[1]]:
        print("No path found")
    else:
        path = []
        while end:
            path.append(end)
            end = parent[end[0]][end[1]]
        print("Path found:", path[::-1])


if __name__ == "__main__":    main()