class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:

        s = str(n)
        L = len(s)
        length = len(digits)

        res = 0
        
    
        for i in range(1,L):
            res += (length ** i)

        @cache
        def solve(index,tight):
            if index == L:
                return 1

            ans = 0
            
            limit = int(s[index]) if tight else int(digits[-1])
          
            for i in digits:
                d = int(i)
               
                if d > limit:
                    continue
                ntight = tight and (d == limit)
             
                ans += solve(index + 1 ,ntight)

            return ans

        return res + solve(0,1)





        