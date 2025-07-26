class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        cuts = [0] + sorted(cuts) + [n]
        m = len(cuts)

        

        dp = [[-1 for i in range(m)] for _ in range(m)]
      


        def dfs(i,j):


            if i +1 == j:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]
            minCost = float("inf")
            for k in range(i+1,j):
                
                cost = dfs(i,k) + dfs(k,j) + (cuts[j] - cuts[i])
                minCost = min(minCost,cost)
            
            dp[i][j] = minCost

            return minCost

        return dfs(0,m-1)



        


