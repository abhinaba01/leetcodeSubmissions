class Solution:

    MOD=1000000007

    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1
        
        else:
            res = self.myPow(x,n//2)
            if n & 1 == 0:
                return (res * res) % self.MOD
            else:
                return (res * x * res) % self.MOD
       
    def countGoodNumbers(self, n: int) -> int:

        nOdd = n // 2
        nEven = (n + 1)// 2
        
        

        res = self.myPow(5,nEven) * self.myPow(4,nOdd)
        return res % (self.MOD)
        