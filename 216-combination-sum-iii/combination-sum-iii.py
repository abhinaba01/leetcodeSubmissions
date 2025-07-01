class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:

        ans = []
        path = []

        def dfs(num,target,i):

            if num == 0 and target == 0:
                ans.append(path[:])
                return
                
         
               

            else:
                for j in range(i,10):
                    path.append(j)
                    
                    dfs(num-1,target-j,j+1)
                    path.pop()

        dfs(k,n,1)
        return ans




           
        


        