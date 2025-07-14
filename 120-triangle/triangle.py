class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        rows = len(triangle)
        column = len(triangle[rows-1])

        dp = [[-1 for _ in range(column)] for _ in range(rows)]

        def dfs(i,j):

            if dp[i][j] != -1:
                return dp[i][j]

            if i == rows - 1:
                dp[i][j] = triangle[i][j]
                return dp[i][j]

                            
            dp[i][j] = triangle[i][j] + min(dfs(i+1,j), dfs(i+1,j+1))
            return dp[i][j]

        return dfs(0,0)


        