class Solution:
    def rob(self, nums: List[int]) -> int:

        
        n = len(nums)

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0],nums[1])
        INF = float("-inf")

        dp = [INF] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        
     

        def f(i):

            if dp[i] != INF:
                return dp[i]

            ans = max(f(i-1), f(i-2) + nums[i])
            
            dp[i] = ans

            return ans

        

        return f(n - 1)

        