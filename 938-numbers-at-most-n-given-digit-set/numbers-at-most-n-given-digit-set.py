class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:

        L = len(digits)

        s = str(n)
        
        MAX = digits[-1]

        res = 0

        for i in range(1,len(s)):
            res += (L ** i)


        @cache
        def dp(pos,tight):

            if pos == len(s):
                return 1
            
            limit = s[pos] if tight else MAX

            ans = 0

            for d in digits:
                if d > limit:
                    continue
                ntight = tight and (d == limit)

                ans += dp(pos + 1,ntight)

            return ans
        
        return res + dp(0,1)
