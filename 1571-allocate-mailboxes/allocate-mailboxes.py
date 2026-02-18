class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:

        n = len(houses)

        houses.sort()


        dp = [[-1] * (k+1) for _ in range(n+1)]



        def cost_segment(i,j):

            cost = 0
            if i == j:
                return 0

            median = houses[(i + j) // 2]

           

            for k in range(i,j+1):
                cost += abs((houses[k] - median))


          

            return cost

        @lru_cache
        def solve(i,m):

           
            if i == n and m == 0:
                return 0


            if i >= n or m == 0:
                return math.inf

            if dp[i][m] != -1:
                
                return dp[i][m]


            ans = math.inf

            
            
            for j in range(i,n):

                ans = min(cost_segment(i,j) + solve(j+1,m-1),ans)
              

            dp[i][m] = ans
            return dp[i][m]


        return solve(0,k)
        
                


        




        