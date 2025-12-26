class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:

        n = len(grid)

        @cache
        def solve(r,c):

            if r >= n or c >= n or c < 0:
                return math.inf

            cost = grid[r][c]

            if r == n - 1:
                return cost

            minPath = math.inf
            for i  in range(n):
                if i == c:
                    continue
                minPath =  min(minPath,solve(r+1,i))
            
            return cost + minPath

        ans = math.inf
        for i in range(n):
            ans = min(ans,solve(0,i))
        
        return ans
            
            
      



        
        