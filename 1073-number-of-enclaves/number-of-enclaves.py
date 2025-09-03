class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
       
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
      


        def bfs(i,j):
            queue = deque([(i,j)])
            
        
            while queue:

                r, c = queue.popleft()
                grid[r][c] = 2

                neighbors = [(0,1),(0,-1),(-1,0),(1,0)]
                for dr,dc in neighbors:
                    if min(r+dr,c+dc) < 0 or r + dr == rows or c + dc == cols or grid[r+dr][c+dc] == 2 or grid[r+dr][c+dc] == 0:
                        continue
                    queue.append((r+dr,c+dc))
                    grid[r+dr][c+dc] = 2

     

        for r in range(rows) :
            for c in [0,cols - 1]:
                if grid[r][c] == 1:
                    bfs(r,c)
        
        for c in range(cols):
            for r in [0,rows - 1]:
                if grid[r][c] == 1:
                    bfs(r,c)

        count = 0        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    count += 1
        
        return  count
        