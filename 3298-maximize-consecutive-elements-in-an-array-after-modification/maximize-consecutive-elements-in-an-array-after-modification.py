

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()

        dp = defaultdict(int)
        ans = 0

        for x in nums:
           
            use_x = dp[x - 1] + 1

          
            use_x_plus_1 = dp[x] + 1

            dp[x] = max(dp[x], use_x)
            dp[x + 1] = max(dp[x + 1], use_x_plus_1)

            ans = max(ans, dp[x], dp[x + 1])

        return ans
