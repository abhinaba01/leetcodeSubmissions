class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        n = len(nums)

        if total % 2 != 0:
            return False
        
        halfSum = total // 2

        dp = {}

        def dfs(i,s):  # is it possible to get subSetSum if we have sum s upto index i ?

            if i == n and s < halfSum:
                return 0
            
            if s == halfSum:
                return 1
            
            if s > halfSum:
                return 0

            if (i,s) in dp:
                return dp[(i,s)]

            if dfs(i+1,s+nums[i]) or dfs(i+1,s):
                dp[(i,s)] = 1
                return 1
            
            else:
                dp[(i,s)] = 0
                return 0

        return True if dfs(0,0) else False



            
                
            


            