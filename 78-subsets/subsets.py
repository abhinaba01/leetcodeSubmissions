


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # n = len(nums)
        # ans = []
        # path = []
      

        # def dfs(start):
        #     ans.append(path[:])
        #     if start == n:
                
              
        #         return
        #     for j in range(start,n):
        #         path.append(nums[j])
        #         dfs(j+1)
        #         path.pop()
        # dfs(0)
        # return ans

        n = len(nums)
        ans = []

        def subSetHelper(index:int,path:List[int]):
            if index == len(nums):
                ans.append(path)
                return
            
            
            path.append(nums[index])
            subSetHelper(index + 1,path[:])
            path.pop()
            subSetHelper(index + 1,path[:])

        subSetHelper(0,[])
        return ans
            


        

