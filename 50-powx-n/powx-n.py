class Solution:
    def myPow(self, x: float, n: int) -> float:

       

      

        if n == 0:
            return 1

        if n == -1:
            return (1/x)
       
        res = self.myPow(x,n//2)
        if n & 1 == 0:
            return res * res
        else:
            return res * x * res
       

       