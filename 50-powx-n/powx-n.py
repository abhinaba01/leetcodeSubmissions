class Solution:
    def myPow(self, x: float, n: int) -> float:

      

      

        if n == 0:
            return 1

        
        elif n > 0:
        
            res = self.myPow(x,n//2)
            if n & 1 == 0:
                return res * res
            else:
                return res * x * res
        
        elif n < 0:
            return 1/(self.myPow(x,-n))
       

       