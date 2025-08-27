class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        path = []

        sorted_candidates = sorted(candidates)

        def dfs(start,n):
            if n < 0:
                return
            elif n == 0:
                ans.append(path[:])
                return ans
            
            for i in range(start,len(sorted_candidates)):
                if i > start and sorted_candidates[i] == sorted_candidates[i - 1]:
                    continue
                path.append(sorted_candidates[i])
                dfs(i+1,n - sorted_candidates[i])
                path.pop()
        
        dfs(0,target)
        return ans

    
        