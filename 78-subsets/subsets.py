class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []
      

        n = len(nums)

        def dfs(j,path):

            if j == n:
                ans.append(path)
                return
            

        
            path.append(nums[j])
            dfs(j+1,path[:])
            path.pop()
            dfs(j+1,path[:])

        dfs(0,[])

        return ans