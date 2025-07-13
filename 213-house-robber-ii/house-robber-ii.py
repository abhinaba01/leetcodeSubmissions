class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
    
        def subrob(nums: List[int]) -> int:

            n = len(nums)

            dp1 = [-1] * (len(nums) + 1)

            def dp(i) -> int:

                if i >= n:
                    return 0
                if dp1[i] != -1:
                    return dp1[i]


                dp1[i] = max(nums[i] + dp(i+2), dp(i+1))
                return dp1[i]


            return dp(0)


        if n == 1:
            return nums[0]


        return max(subrob(nums[1:]),subrob(nums[0:n-1]))
        