from math import gcd
from typing import List

MOD = 10 ** 9 + 7

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        mx = max(nums)

        dp = [[0] * (mx + 1) for _ in range(mx + 1)]
        dp[0][0] = 1

        for x in nums:
            ndp = [row[:] for row in dp]

            for g1 in range(mx + 1):
                for g2 in range(mx + 1):
                    cur = dp[g1][g2]
                    if cur == 0:
                        continue

                    ng1 = gcd(g1, x)
                    ndp[ng1][g2] = (ndp[ng1][g2] + cur) % MOD

                    ng2 = gcd(g2, x)
                    ndp[g1][ng2] = (ndp[g1][ng2] + cur) % MOD

            dp = ndp

        ans = 0
        for g in range(1, mx + 1):
            ans = (ans + dp[g][g]) % MOD

        return ans