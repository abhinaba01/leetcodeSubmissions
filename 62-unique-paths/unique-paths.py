class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[-1] * n for _ in range(m)]

        def count(r,c):

           

            if r == m or c == n:
                return 0

            if r == m - 1 and c == n - 1:
                return 1

            if dp[r][c] != -1:
                return dp[r][c]


            dp[r][c] = count(r+1,c) + count(r,c+1)
            return dp[r][c]

        
        return count(0,0)


       