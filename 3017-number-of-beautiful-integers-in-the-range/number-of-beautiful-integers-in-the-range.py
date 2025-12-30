class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:

        def countIntegers(n):

            s = str(n)
            L = len(s)

            # dp = [[[[[-1 for _ in range(2)]
            #             for _ in range(k+1)]
            #             for _ in range(2)]
            #             for _ in range(2)]
            #             for _ in range(L)]

            @cache
            def solve(pos,tight,diff,rem,valid):

                if pos == L:
                    if rem == 0 and diff == 0:
                        return 1
                    else:
                        return 0

                # if dp[pos][tight][diff][rem][valid] != -1:
                #     return dp[pos][tight][diff][rem][valid]

                ans = 0
                
                limit = int(s[pos]) if tight else 9

                for d in range(limit+1):
                    ntight = tight and (d == limit)
                    nvalid = valid or ( d != 0)

                    nrem = (rem * 10 + d) % k
                    ndiff = diff
                    if d == 0 and nvalid:
                        ndiff += 1
                    if d != 0:
                        if d % 2 == 0:
                            
                            ndiff += 1
                        else:
                            ndiff -= 1

                    ans += solve(pos + 1,ntight,ndiff,nrem,nvalid)
                # dp[pos][tight][diff][rem][valid] = ans
                
                return ans 
            
            return solve(0,1,0,0,False)

        return countIntegers(high) - countIntegers(low - 1)

                



            