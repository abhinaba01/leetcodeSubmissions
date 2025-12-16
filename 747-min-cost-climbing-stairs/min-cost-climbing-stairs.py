class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        dp = [-1] * (n + 1) 

        def costClimb(i):
            if i >= n:
                return 0


            if dp[i] != -1:
                return dp[i]
            else:
                dp[i] =  cost[i] + min(costClimb(i+1), costClimb(i+2))
                return dp[i]
            
                
        return min(costClimb(0),costClimb(1))
        


        