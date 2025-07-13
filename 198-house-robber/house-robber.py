class Solution:

    
    def rob(self, nums: List[int]) -> int:


        
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
        







        

        



        