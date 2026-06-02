class Solution:
    def beautifulNumbers(self, l: int, r: int) -> int:


        def solve(num):

            s = str(num)
            L = len(s)

        
            memo = {}
            def dp(pos,tight,sumD,prod,valid):

                if pos == L:

                    if sumD == 0 or prod % sumD != 0:
                        return 0
                    else:
                        return 1

                if (pos,tight,sumD,prod,valid) in memo:
                    return memo[(pos,tight,sumD,prod,valid)]
                
                limit = s[pos] if tight else 9
                limit = int(limit)

                cnt = 0

                for d in range(limit + 1):

                    ntight = tight and (d == limit)
                    nvalid = valid or (d != 0)
                    
                    if not nvalid:
                        cnt += dp(pos+1,ntight,sumD+ d,prod,nvalid)
                    else:
                        cnt += dp(pos+1,ntight,sumD + d,prod * d,nvalid)

                memo[(pos,tight,sumD,prod,valid)] = cnt
                    
                return cnt

            return dp(0,1,0,1,False)


        return solve(r) - solve(l - 1)

        