class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:

        MOD = 10 ** 9 + 7

        def count(x):

            return (x // a + x // b - x // lcm(a ,b)) 

        
        low , high = 1 , min(a,b) * n
        ans  = -1

        while low <= high:

            mid = (low + high) // 2
            if count(mid) >= n:
                high = mid - 1
                ans = mid
            
            else:
                low = mid + 1


        return ans % MOD

        