class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n > 0:
            res = n & (n-1)
            return res == 0
        
        else:
            return False
            

        
        