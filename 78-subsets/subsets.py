


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        ans = []
        path = []

        def dfs(start):
            ans.append(path[:])
            if start == n:
                return
            for j in range(start,n):
                path.append(nums[j])
                dfs(j+1)
                path.pop()
        dfs(0)
        return ans

