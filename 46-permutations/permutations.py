class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        res = []


        def dfs(arr):

      
            if not  arr:
                ans.append(res[:])
                return

            
           
            for j in range(len(arr)):
                res.append(arr[j])
                dfs(arr[:j] + arr[j+1:])
                res.pop()

            
        
        dfs(nums)
        return ans


            



