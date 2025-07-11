class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
    

        max_farthest = 0
        for i in range(n):

            if i > max_farthest:
                return False
            max_farthest = max(i+nums[i],max_farthest)

        return True
            

        

        # def dfs(i):

        #     if arr[i] == 0:
        #         return False

        #     if i >= n-1:
        #         return True
               
        #     if i < (n-1) and nums[i] == 0:
        #         arr[i] = 0
        #         return False

        #     for j in range(1,nums[i] + 1):
                
        #         if dfs(i+j):
        #             return True

        #     arr[i] = 0

            
        #     return False

        # return dfs(0)





            