class Solution:

            
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

      
        ans = []

        def dfs (start,target,path):

            if target == 0:
                
              
                ans.append(path[:])

            elif target < 0:
                return

            else: 
                
                for i in range(start,len(candidates)):
                    path.append(candidates[i])
                    dfs(i,target-candidates[i],path)
                    path.pop()

        dfs(0,target,[])

          
        return ans 
            
        



        