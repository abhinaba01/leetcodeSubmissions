class Solution:
    def countBalanced(self, low: int, high: int) -> int:

        def solve(num):

            s = str(num)
            L = len(s)

            memo = {}
            def dp(pos,index,tight,sumD):

                if pos == L:
                    if sumD == 0:
                        return 1
                    else:
                        return 0


                if (pos,index,tight,sumD) in memo:
                    return memo[(pos,index,tight,sumD)]

                limit = s[pos] if tight else 9 
                limit = int(limit)

                cnt = 0

                for d in range(limit + 1):

                    ntight = tight and (d == limit)

                    if index:
                        cnt += dp(pos + 1,(index + 1) % 2,ntight,sumD + d)
                    else:
                        cnt += dp(pos + 1,(index + 1) % 2,ntight,sumD - d)

                memo[(pos,index,tight,sumD)] = cnt
                return cnt

            return dp(0,1,1,0)

        high = high 
        low = max(9,low - 1)

        return (solve(high) - solve(low))

            
            