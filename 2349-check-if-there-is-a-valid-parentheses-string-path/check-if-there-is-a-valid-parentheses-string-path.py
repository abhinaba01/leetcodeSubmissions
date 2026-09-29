class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:

        rows = len(grid)
        cols = len(grid[0])

        dire = [(0,1) , (1,0)]

        dp = {}


        @cache
        def dfs(r ,c ,balance):

            if (r ,c ,balance) in dp:
                return dp[(r,c,balance)]

            if grid[r][c] == '(':
                balance += 1
                
            else:
                balance -= 1

            if balance < 0:
                dp[(r,c,balance)] = False
                return False
        
            
            if r == rows - 1 and c == cols - 1:
                dp[(r,c,balance)] = (balance == 0)
                return dp[(r,c,balance)]
             
            for dr , dc in dire:
                nr = r + dr
                nc = c + dc

                if not (0 <= nr < rows and 0 <= nc < cols):
                    continue

               

                if dfs(nr , nc, balance):
                    return True

            dp[(r,c,balance)] = False
            return dp[(r,c,balance)]

        return dfs(0,0,0)




            




        