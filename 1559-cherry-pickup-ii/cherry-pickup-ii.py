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

            best = -math.inf
            for dc1 in (-1,0,1):
                for dc2 in (-1,0,1):
                    best =  max(best , solve(r+1,c1 + dc1,c2 + dc2))

         
            ans = cherries + best
            return ans
        
        return solve(0,0,cols - 1)
            






        