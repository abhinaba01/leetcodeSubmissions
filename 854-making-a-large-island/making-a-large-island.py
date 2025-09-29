

class Solution:
    def largestIsland(self, grid):
        n = len(grid)
        island_size = {}   # id -> size
        island_id = 2      # start ids from 2 so they don’t conflict with 0/1

        # BFS to label an island and count its size
        def bfs(i, j, id_):
            q = deque([(i, j)])
            grid[i][j] = id_
            size = 1

            while q:
                x, y = q.popleft()
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = id_
                        q.append((nx, ny))
                        size += 1
            return size

        # 1. Label all islands and store their sizes
        max_island = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size = bfs(i, j, island_id)
                    island_size[island_id] = size
                    max_island = max(max_island, size)
                    island_id += 1

        # 2. Try flipping each 0 and compute potential island size
        result = max_island
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighbor_ids = set()
                    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                        ni, nj = i + dx, j + dy
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            neighbor_ids.add(grid[ni][nj])
                    new_size = 1 + sum(island_size[id_] for id_ in neighbor_ids)
                    result = max(result, new_size)

        # 3. Handle edge case: all ones
        return result if result > 0 else n * n


    