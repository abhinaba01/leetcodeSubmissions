class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        path = []
        

        n = len(candidates)
        candidates.sort()

        def solve(i,rem):

            if rem < 0:
                return
            
            if rem == 0:
                res.append(path[:])
                

            for j in range(i,n):

                if j > i and candidates[j] == candidates[j-1]:
                    continue

                
                
                path.append(candidates[j])
                solve(j+1,rem - candidates[j])
                path.pop()

        solve(0,target)
        return res

        