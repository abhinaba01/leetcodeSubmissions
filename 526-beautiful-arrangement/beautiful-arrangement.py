class Solution:
    def countArrangement(self, n: int) -> int:



        def valid(x,position):
            if x % position == 0 or position % x == 0:
                return True
            
            return False
        
       
        dp = [0] * (1 << n)
        dp[0] = 1

        for mask in range(1 << n):

            pos = mask.bit_count() + 1

            for i in range(n):

                if not (mask & (1 << i)):

                    if valid(i + 1, pos):
                        dp[mask | (1 << i)] += dp[mask]

        
        return dp[(1<<n) - 1]