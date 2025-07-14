class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        dp = [[-1 for _ in range(n)] for _ in range(m)] 

    

        def dfs(i,j):

            if dp[i][j] != -1:
                return dp[i][j]

            if i == m -1 and j == n -1:
                dp[i][j] = grid[i][j]
                return dp[i][j]


            if i + 1 < m and j + 1 < n:
                dp[i][j] =  (grid[i][j] + min(dfs(i,j+1) , dfs(i+1,j)))
                return dp[i][j]

            if i + 1 < m and j + 1 >=n:
                dp[i][j] =  (grid[i][j] + dfs(i+1,j))
                return dp[i][j]

            if j + 1 < n and i + 1 >= m:
                dp[i][j] = (grid[i][j] + dfs(i,j+1))
                return dp[i][j]


        return dfs(0,0)

        
        