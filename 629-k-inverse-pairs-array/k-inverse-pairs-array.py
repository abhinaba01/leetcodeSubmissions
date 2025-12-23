class Solution:
    def kInversePairs(self, n: int, k: int) -> int:

        dp = [[-1] * (k+1) for _ in range(n+1)]
        MOD = 10 ** 9 + 7

        def rec(a,b):

            if b == 0:
                return 1
            
            if a <= 0 or b < 0:
                return 0 
            
            if dp[a][b] != -1:
                return dp[a][b]

            
            dp[a][b] = (rec(a-1,b) + rec(a,b-1) - rec(a-1,b-a)) % MOD
         
            return dp[a][b]
        return rec(n,k)

            



        