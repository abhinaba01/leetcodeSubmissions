class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        visit = set()

        def dfs(i,j):
            
            if (min(i,j) < 0 or i == rows or j == cols or (i,j) in visit or grid[i][j] == 0):
                return 0
            
            visit.add((i,j))
            area = 1 +  dfs(i-1,j) + dfs(i+1,j) + dfs(i,j-1) + dfs(i,j+1)
            
            return area

        maxArea = 0

        for r in range(rows) :
            for c in range(cols):
                if grid[r][c] == 1:
                    if (r,c) not in visit:
                        maxArea = max(maxArea,dfs(r,c))
        
        return maxArea

        