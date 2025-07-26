class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]
        n = len(nums)

        @lru_cache(None)
        def dfs(i,j):

            if i+1 == j:
                return 0

            maxCost = 0
            for k in range(i+1,j):
               
                cost =  (nums[i] * nums[k] * nums[j])  + dfs(i,k) + dfs(k,j) 
                maxCost = max(maxCost,cost)

            return maxCost
        
        return dfs(0,n-1)


        