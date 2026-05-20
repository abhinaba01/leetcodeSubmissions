class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        n = len(coins)


        def lcm(a,b):
            return a * b // gcd(a,b)


        def f(val):

            total = 0
            cnt = 0

            

            for mask in range(1,1 << n):
                                  
                a = 1
                c = 0

                for i in range(n):
                    if mask & (1<<i):
                        a = lcm(a,coins[i])
                        c += 1
                
              

                cnt = (val // a) 
               
              
                if c % 2 == 0:
                    total -= cnt
                else:
                    total += cnt
         
        
            return total >= k

                
                

                

            


        





        low , high = min(coins) , max(coins) * (k + 1)

        ans = -1


        while low <= high:
            mid = low + (high - low) // 2
            if f(mid):
                ans = mid 
                high = mid - 1
            else:
                low = mid + 1

        return ans
