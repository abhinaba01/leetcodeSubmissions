class Solution:
    def specialPerm(self, nums: List[int]) -> int:

        MOD = 10 ** 9 + 7

        n = len(nums)

        def isValid(pos,last):
            if (nums[pos] % nums[last] == 0 or nums[last] % nums[pos] == 0):
                return True

            return False

        dp = [[0] * n for _ in range(1 << n)]
        
        for i in range(n):
            dp[1 << i][i] = 1
        
        for mask in range(1,1 << n):

            for prev in range(n):

                if not (mask & (1 << prev)):
                    continue

                for i in range(n):
                    if (mask & (1 << i)):
                        continue

                    if isValid(i,prev):
                        dp[mask | (1 << i)][i] += dp[mask][prev]
                        dp[mask | (1 << i)][i] %= MOD



        return sum(dp[(1 << n) - 1]) % MOD



        