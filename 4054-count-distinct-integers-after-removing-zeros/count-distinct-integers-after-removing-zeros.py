class Solution:
    def countDistinct(self, n: int) -> int:

        s = str(n)
        L = len(s)

        @cache
        def solve(pos,tight,started):

            if pos == L:
                return 1
            
            ans = 0

            limit = int(s[pos]) if tight else 9
            for d in range(limit + 1):
                ntight = tight and (d == limit)
                nstarted = started or (d != 0)

                if started and d == 0:
                    continue
                
                ans += solve(pos + 1,ntight,nstarted)

            return ans

        return solve(0,1,False) - 1

        
        