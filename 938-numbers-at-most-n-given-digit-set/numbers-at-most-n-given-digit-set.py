class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:

        L = len(digits)

        s = str(n)
        
        MAX = digits[-1]

        res = 0

        for i in range(1,len(s)):
            res += (L ** i)

        
        memo = {}
        def dp(pos,tight):

            if pos == len(s):
                return 1

            if (pos,tight) in memo:
                return memo[(pos,tight)]

            
            limit = s[pos] if tight else MAX

            ans = 0

            for d in digits:
                if d > limit:
                    continue
                ntight = tight and (d == limit)

                ans += dp(pos + 1,ntight)

            memo[(pos,tight)] = ans
            return memo[(pos,tight)]

        
        return res + dp(0,1)
