class Solution:
    def findComplement(self, num: int) -> int:
        
        n = num
        i = 0

        while n != 0:
            i += 1
            n = n >> 1
        
        return ((2**i) - 1 ^ num)

         