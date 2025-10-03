class Solution:
    def jump(self, nums: List[int]) -> int:

        n = len(nums)
        maxPos = n - 1
        i = 0
        count = 0

        while maxPos != 0:
          

            i = 0

            for i in range(maxPos):
               
                if i + nums[i] >= maxPos:
                    maxPos = i
                    count += 1
                    break
                
                           
        
        return count



        