class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        sumArr = sum(nums)
        if sumArr & 1 != 0:
            return False

        target = sumArr // 2
        n = len(nums)

        dp = {}

        def dfs(i,currentSum):

            if currentSum == 0:
                
                return True

            if (i,currentSum) in dp:
                return dp[(i,currentSum)]

            if i == n or currentSum < 0:
                return False
            
            dp[(i,currentSum)] = dfs(i+1,currentSum-nums[i]) or dfs(i+1,currentSum)
            return dp[(i,currentSum)]

        return dfs(0,target)

                


            
        