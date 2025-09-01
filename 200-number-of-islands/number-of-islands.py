class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        def dfs(i,j,visit):
            if (min(i,j) < 0 or i == rows or j == cols or (i,j) in visit or grid[i][j] == '0'):
                return
            
            visit.add((i,j))

            
            dfs(i-1,j,visit)
            dfs(i+1,j,visit)
            dfs(i,j-1,visit)
            dfs(i,j+1,visit)

            return 
        
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    if (r,c) not in visit:
                        dfs(r,c,visit)
                        count += 1
                        
        return count
        