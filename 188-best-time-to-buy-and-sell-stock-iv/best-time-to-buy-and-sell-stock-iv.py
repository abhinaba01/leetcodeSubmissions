class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        n = len(prices)
        
        dp = [[[float("-inf")] * (k+1) for _ in range(2)] for _ in range(n + 1)]

        for i in range(n):
            dp[i][0][0] = 0
        dp[0][1][1] = - prices[0]

        for i in range(1,n):

            for j in range(1,k+1):
             
                dp[i][1][j] = max(dp[i-1][1][j], dp[i-1][0][j-1] - prices[i])
                dp[i][0][j] = max(dp[i-1][0][j] , dp[i-1][1][j] + prices[i] )
               
        
        return max(dp[n-1][0])