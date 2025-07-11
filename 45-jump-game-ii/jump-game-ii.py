class Solution:
    def jump(self, nums: List[int]) -> bool:
        n = len(nums)
    
        max_farthest = 0
        cnt = 0
        current_end = 0
        for i in range(n-1):

            max_farthest = max(i+nums[i],max_farthest)

            if i == current_end:
                cnt += 1
                current_end = max_farthest
        return cnt
        
            
