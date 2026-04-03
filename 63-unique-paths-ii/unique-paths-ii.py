class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:


        m = len(obstacleGrid)
        n = len(obstacleGrid[0])


        dp = [[-1] * n for _ in range(m)]

        def count(r,c):

            if r == m or c == n:
                return 0

            if obstacleGrid[r][c] == 1:
                return 0
            
            if r == m - 1 and c == n - 1:
                return  1

            if dp[r][c] != -1:
                return dp[r][c]

            dp[r][c] =  count(r+1,c) + count(r,c+1)
            return dp[r][c]
        
        return count(0,0)


       