class Solution:

    def myPow(self, x: float, n: int) -> float:

        MOD=1000000007

        if n == 0:
            return 1
        
        else:
            res = self.myPow(x,n//2)
            if n & 1 == 0:
                
                return (res * res) % MOD
            else:
                 return (res * x * res) % MOD
       
    def countGoodNumbers(self, n: int) -> int:

        MOD=1000000007

        
        nOdd = n // 2
        nEven = (n + 1 )// 2
        res = 0
        

        res = self.myPow(5,nEven) * self.myPow(4,nOdd)
        return res % (MOD)
        