class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        
        n = len(prices)
        
        dp = [[[float("-inf")]  for _ in range(2)] for _ in range(n + 1)]

        for i in range(n):
            dp[i][0] = 0
        dp[0][1] = - prices[0]

        for i in range(1,n):

           
             
                dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
                dp[i][0] = max(dp[i-1][0] , dp[i-1][1] + prices[i] - fee )
               
        
        return max(dp[n-1])

        
        