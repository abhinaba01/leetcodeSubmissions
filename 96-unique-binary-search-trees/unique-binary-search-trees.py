class Solution:
    def numTrees(self, n: int) -> int:
        
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
       

        for x in range(2,n+1):
            for k in range(1,x+1):
                dp[x] += (dp[k-1] * dp[x-k])

        return dp[n]
