class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        n = len(grid)
        queue = [(0,0)]
        visited = set()
        visited.add((0,0))

        length = 1

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        neighbors = [(-1,0),(1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]

        while queue:
            for i in range(len(queue)):
                r,c = queue.pop(0)

                if r == n - 1 and c == n - 1:
                    return length
                

                for dr,dc in neighbors:
                    if min(r+dr,c+dc) < 0 or (r+dr) == n or (c + dc) == n or (r+dr,c+dc) in visited or grid[r+dr][c+dc] == 1:
                        continue
                    
                    queue.append((r+dr,c+dc))
                    visited.add((r+dr,c+dc))

            length += 1
        
        return -1
        
            







    
        