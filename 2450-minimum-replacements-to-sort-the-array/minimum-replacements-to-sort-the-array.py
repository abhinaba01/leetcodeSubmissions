class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:

        n = len(nums)
        last = nums[-1]
        ans = 0

        for i in range(n - 2,-1,-1):

            

          
            steps = ceil(nums[i] / last)
            last = floor(nums[i] / steps)
        

            ans += (steps - 1)

        return ans
         
        
        



             

            

        