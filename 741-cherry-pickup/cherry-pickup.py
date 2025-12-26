class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        n = len(grid)

        @cache
        def dfs(r1,c1,r2):

            c2 = r1 + c1 - r2

            if r1 > n -1 or c1 > n - 1 or r2 > n - 1 or c2 > n - 1:
                return float("-inf")
            
            else:

                if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                    
                    return float("-inf")
                
                if r1 == n-1 and c1 == n-1:
                    return grid[r1][c1]



                cnt = 0

                cnt += grid[r1][c1]
              
                if (r1,c1) != (r2,c2):
                    cnt += grid[r2][c2]
                  

                return cnt + max(dfs(r1+1,c1,r2+1) , 
                                dfs(r1,c1+1,r2+1) , 
                                dfs(r1+1,c1,r2) , 
                                dfs(r1,c1+1,r2))

        ans =  dfs(0,0,0) 
        return 0 if ans == float("-inf") else ans
            


          
           
           
           
           
           
           
           
       