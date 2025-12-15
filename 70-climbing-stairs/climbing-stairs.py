class Solution:
    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1

        steps = [-1] * (n+1)
        steps[1] = 1
        steps[2] = 2

        def dp(n):

           

            if steps[n] != -1:
                return steps[n]
            
            else:

                steps[n] =  dp(n-1) + dp(n-2)
                return steps[n]
        return dp(n)    