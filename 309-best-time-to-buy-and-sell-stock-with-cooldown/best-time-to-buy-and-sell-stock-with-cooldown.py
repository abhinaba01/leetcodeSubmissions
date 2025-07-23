class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        dp = [[-1 for _ in range(n)] for _ in range(2)]

        def dfs(ind,buy):


            if ind == n or ind == n + 1:
                return 0

            if dp[buy][ind] != -1:
                return dp[buy][ind]

            if buy == 1:
                profit = max(prices[ind] + dfs(ind + 2, 0), dfs(ind+1,1))

            else:
                profit = max(-prices[ind] + dfs(ind+1,1),dfs(ind+1,0))

            dp[buy][ind] = profit
            return profit
        
        return dfs(0,0)

        


        