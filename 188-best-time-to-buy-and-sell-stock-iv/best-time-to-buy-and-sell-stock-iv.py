class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        n = len(prices)
        dp = [[[-1 for i in range(n)] for _ in range(2)] for _ in range(k+1)]

        def dfs(ind,buy,k):

            if ind == n or k == 0:
                return 0


            if dp[k][buy][ind] != -1:
                return dp[k][buy][ind]

            if buy == 1:
                profit =  max(prices[ind] + dfs(ind+1,0,k-1), dfs(ind+1,1,k))
            else:
                profit = max(-prices[ind] + dfs(ind+1,1,k), dfs(ind+1,0,k))

            dp[k][buy][ind] = profit
            return profit
        
        return dfs(0,0,k)

        