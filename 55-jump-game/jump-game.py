class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        maxLength = 0

        for i in range(n):
            if i > maxLength:
                return False
            maxLength = max(maxLength,i + nums[i])
        
        return True


        