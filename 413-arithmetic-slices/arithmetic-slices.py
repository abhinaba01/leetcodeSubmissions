class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:

        n = len(nums)
        count = 0
        curr_len = 0

        if n <= 2:
            return 0

        for i in range(2,n):

            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                curr_len += 1
                count += curr_len
            else:
                curr_len = 0
        
        return count
                
                

        
       

        
        