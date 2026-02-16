class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        path = []
        
        
        def solve(arr,path):
            
            if len(path) == len(nums):
                res.append(path)
           
           
            
            n = len(arr)

            for i in range(n):
                path.append(arr[i])
                solve(arr[:i] + arr[i+1:],path[:])
                path.pop()

        solve(nums,path)
        return res

        