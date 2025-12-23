class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
       
        dp = [[[float("-inf")] * 3 for _ in range(3)] for _ in range(n + 1)]

        for i in range(n):
            dp[i][0][0] = 0
        dp[0][1][1] = - prices[0]

        for i in range(1,n):
             
                dp[i][1][1] = max(dp[i-1][1][1], dp[i-1][0][0] - prices[i])
                dp[i][0][1] = max(dp[i-1][0][1] , dp[i-1][1][1] + prices[i] )
                dp[i][1][2] = max(dp[i-1][1][2], dp[i-1][0][1] - prices[i])
                dp[i][0][2] = max(dp[i-1][0][2] , dp[i-1][1][2] + prices[i] )
        
        return max(dp[n-1][0])
