from typing import List

class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:

        K = len(slices) // 3   # GLOBAL required picks
        NEG = -10**15

        def solve(arr: List[int]) -> int:
            n = len(arr)

            dp = [[[NEG]*2 for _ in range(K+1)] for _ in range(n)]

            dp[0][0][0] = 0
            dp[0][1][1] = arr[0]

            for i in range(1, n):
                for k in range(0, K+1):
                    # not take
                    dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1])

                    # take
                    if k > 0:
                        dp[i][k][1] = dp[i-1][k-1][0] + arr[i]

            return max(dp[n-1][K][0], dp[n-1][K][1])

        # circular handling
        return max(
            solve(slices[:-1]),  # exclude last
            solve(slices[1:])    # exclude first
        )
