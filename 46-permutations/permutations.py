class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        ans = []
        path = []

        def dfs(new_nums):

            if len(path) == n:
                ans.append(path[:])
                return

            N = len(new_nums)
            for j in range(N):
                path.append(new_nums[j])
                dfs(new_nums[:j]+new_nums[j+1:])
                path.pop()

        dfs(nums[:])
        return ans

            


           
            







    