class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        n = len(arr)

        dp = [-1 for _ in range(n+1)]

        def dfs(i):
         
            if i == n:
                return 0

            if dp[i] != -1:
                return dp[i]
            maxCost = 0
            maxVal = 0
            for j in range(i,min(i+k,n)):
              
                maxVal  = max(maxVal,arr[j])
                cost = maxVal * (j+1-i) + dfs(j+1)
                maxCost = max(maxCost,cost)
            
            dp[i] = maxCost
            return maxCost

        return dfs(0)