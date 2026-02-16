class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        path = []

        n = len(candidates)


        def solve(i):

            if target - sum(path) < 0:
                return 

            if target - sum(path) == 0:
                res.append(path[:])
                

            for j in range(i,n):
       
                path.append(candidates[j])
                solve(j)
                path.pop()

        solve(0)
        return res


            
        