from functools import lru_cache

class Solution:
    def countDigitOne(self, n: int) -> int:
        s = str(n)
        L = len(s)

        @lru_cache(None)
        def dp(pos, tight):
           
            if pos == L:
                return (1, 0)   

            limit = int(s[pos]) if tight else 9
            total_nums = 0
            total_ones = 0

            for d in range(limit + 1):
                ntight = tight and (d == limit)
                nums, ones = dp(pos + 1, ntight)

                total_nums += nums
                total_ones += ones

                if d == 1:
                    total_ones += nums  

            return (total_nums, total_ones)

        return dp(0, True)[1]



            

