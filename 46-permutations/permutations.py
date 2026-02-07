class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        ans = []

        
        def dfs(nums,path):

            if not nums:
                ans.append(path)
                return

            for i in range(len(nums)):
                dfs(nums[:i] + nums[i+1:],path + [nums[i]])

        dfs(nums,[])

        
        return ans

