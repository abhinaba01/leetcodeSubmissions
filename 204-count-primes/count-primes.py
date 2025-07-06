class Solution:
    def countPrimes(self, n: int) -> int:

        if n == 0 or n == 1:
            return 0

        prime = [1] * (n)

        for i in range(2,(n//2 +1)):
            if prime[i] == 1:
                for j in range(i*i,n,i):
                    prime[j] = 0

        return prime.count(1) - 2



        

       
        

        


        


        
        


        

        
        