class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        
        if n & (n-1) == 0:

            i = 0

            while n != 0:
                n >>= 1
                i += 1
            
            if i % 2 == 1:
                return True
            
            return False
        
        return False
        


     

        