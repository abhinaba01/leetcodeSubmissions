class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:

        

        def f(val):

            cnt = 0

            for i in range(1, m + 1):

                cnt += min(n, val // i)

            return cnt >= k

                  

           

        

        low , high = 1 , (m * n)
        ans  = -1 

        while low <= high:
            mid = low + (high - low) // 2
            if f(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        
        return ans
                
