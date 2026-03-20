class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:


        n = len(hats)

        # dp = [[-1] * (1 << n) for _ in range(40)]


        MOD = 10 ** 9 + 7

        


        @lru_cache(None)
        def solve(hat,mask):

            if mask == (1<<n) - 1:
                return 1
            
            if hat > 40:
                return 0
            

            # if dp[i][mask] != -1:
            #     return dp[i][mask]

            
            cnt = solve(hat+1,mask) % MOD

           
            

            for j in range(n):

                if not mask & (1 << j):


                    if hat in hats[j]:

                        cnt = (cnt + solve(hat+1,(mask | ( 1<< j))) ) % MOD

            
            # dp[i][mask] =  cnt
            return cnt % MOD

        
        return solve(1,0)

        