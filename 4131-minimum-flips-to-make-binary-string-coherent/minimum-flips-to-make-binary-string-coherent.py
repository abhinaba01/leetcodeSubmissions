class Solution:
    def minFlips(self, s: str) -> int:

        n = len(s)
        if n < 3:
            return 0

        cnt = 0

        ones = s.count("1")
        zeros = n - ones

        if zeros == 0 or ones <= 1:
            return 0
        
        

        if ones >= 2:
            if s[0] == '1' and s[-1] == '1':
                return min(zeros,ones - 2,ones , ones - 1)

            else:
                return min(zeros,ones , ones - 1)

         
       