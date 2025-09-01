from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        fresh = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0        

        neighbors = [(-1,0),(1,0),(0,-1),(0,1)]
        
        time = 0
        while queue:
            for i in range(len(queue)):
                r ,c = queue.popleft()

                for dr,dc in neighbors:
                    if min(r+dr,c+dc) < 0 or (r+dr) == rows or (c + dc) == cols or grid[r+dr][c+dc] == 2 or grid[r+dr][c+dc] == 0:
                        continue
                    queue.append((r+dr,c+dc))
                    grid[r+dr][c+dc] = 2
                    fresh -= 1
                
            time += 1
        
        time -= 1

        return time if fresh == 0 else -1

            

      

            

        


        