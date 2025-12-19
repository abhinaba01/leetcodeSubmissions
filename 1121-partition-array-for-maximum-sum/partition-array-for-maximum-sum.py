class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(1,n+1):
            for j in range(1,min(i,k)+1):
               
                dp[i] = max(dp[i-j] + max(arr[i-j:i])*j,dp[i])
        return dp[n]

        