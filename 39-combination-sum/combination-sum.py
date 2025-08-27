class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        path = []

        def dfs(start,n):
            if n < 0:
                return
            if n == 0:
                ans.append(path[:])
                return
            
            for i in range(start,len(candidates)):
                path.append(candidates[i])
                dfs(i,n - candidates[i])
                path.pop()

        dfs(0,target)
        return ans

        