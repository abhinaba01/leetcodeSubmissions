class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        lastDay = days[-1]

        dp = [0] * (lastDay + 1)
        dp[0] = 0
        
        k = 1

        for i in range(1,lastDay+1):
            if i not in days:
                dp[i] = dp[k]

            else:
                dp[i] = min(dp[max(0,i-1)]+costs[0],dp[max(0,i-7)]+costs[1],dp[max(0,i-30)]+costs[2])
                k = i
        print(dp)
        return dp[lastDay]

