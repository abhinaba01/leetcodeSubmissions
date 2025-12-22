class Solution:
    def checkRecord(self, n: int) -> int:

      

        MOD = 10 ** 9 + 7

        dp = [[[-1 for _ in range(3)] 
            for _ in range(2)] 
            for _ in range(n+1)]

        
        def rec(k,A,L): 
            
            if k == 0:
                return 1
        

            if dp[k][A][L] != -1:
                return dp[k][A][L]
                
            else:

                if A == 0:
                    ans = (rec(k-1,A , 0) + rec(k-1,A+1,0) ) % MOD
                    if  L < 2:
                        ans = (ans + rec(k-1,A,L+1)) % MOD
                   
                else:
                    ans = rec(k-1,A,0) % MOD
                    if L < 2:
                        ans =( ans +  rec(k-1,A,L+1)) % MOD

            dp[k][A][L] = ans

            return ans
        
        return rec(n,0,0)







        
        