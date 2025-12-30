class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:

        MOD = 10 ** 9 + 7
        
        @cache
        def countInteger(n):

            MOD = 10 ** 9 + 7

            
            L = len(n)
            @cache
            def solve(pos,tight,valid,sumd):
                
                if pos == L:
                    if sumd <= max_sum and sumd >= min_sum:
                        return 1
                    else:
                        return 0
                
                ans = 0
                
                limit = int(n[pos]) if tight else 9
                for d in range(limit + 1):
                    ntight = tight and (d == limit)
                    nvalid = valid or (d != 0)
                    
                    ans = (ans +  solve(pos+1,ntight,nvalid,sumd + d)) % MOD

                return ans
            
            return solve(0,1,False,0)

        return abs((countInteger(num2) - countInteger(str(int(num1) - 1))) % MOD)

            
            