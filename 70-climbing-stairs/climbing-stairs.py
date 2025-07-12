class Solution:

    dp = [-1] * (100)
    def climbStairs(self, n: int) -> int:

        if self.dp[n] != -1:
            return self.dp[n]

        

        if n == 1:
            return 1
        if n == 0:
            return 1

        self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dp[n]




        