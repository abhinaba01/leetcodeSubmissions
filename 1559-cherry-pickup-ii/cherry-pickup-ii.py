class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        @cache
        def solve(r,c1,c2):

            if r >= rows or c1 >= cols or c2 >= cols or c1 < 0 or c2 < 0:
                return -math.inf

            cherries = 0
            

            cherries += grid[r][c1]
           
            if c1 != c2:
                cherries += grid[r][c2]
          
            
            if r == rows - 1:
                return cherries

            

            ans =   cherries + max( solve(r+1,c1-1,c2-1),solve(r+1,c1-1,c2),solve(r+1,c1-1,c2+1),
                        solve(r+1,c1,c2-1),solve(r+1,c1,c2),solve(r+1,c1,c2+1),
                        solve(r+1,c1+1,c2-1),solve(r+1,c1+1,c2),solve(r+1,c1+1,c2+1)
            )

            return ans
        
        return solve(0,0,cols - 1)
            






        