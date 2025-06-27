class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1
        elif n==1:
             return x
        elif n==-1:
             return 1/x
    
        else:
            res = self.myPow(x,n//2)
            if n & 1 == 0:
                
                return res * res
            else:
                 return res * x * res
       