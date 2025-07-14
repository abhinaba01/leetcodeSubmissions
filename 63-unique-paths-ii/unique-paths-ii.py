class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:


        
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[-1 for _ in range(m)] for _ in range(n)] 
        
        
        
        def dfs(i,j):
            
            
            if i >= n or j >= m:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
                
            
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
                return dp[i][j]
                
            if i == n - 1 and j == m - 1:
                return 1
                
            
            down = dfs(i,j+1)
            right = dfs(i+1,j)
            
            dp[i][j] = down + right
                    
            return dp[i][j]
            
        
          
        a = dfs(0,0)
        
        return a
        
            
        
                
        