class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        rows = len(grid)
        cols = len(grid[0])

       

        dire = [(0, 1), (1, 0)]
        dp = {}

        def dfs(r, c, balance):
           
            if grid[r][c] == '(':
                balance += 1
            else:
                balance -= 1

           
            if balance < 0:
                return False
          

         
            if (r, c, balance) in dp:
                return dp[(r, c, balance)]
            
           
            if r == rows - 1 and c == cols - 1:
                return balance == 0
             
         
            for dr, dc in dire:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if dfs(nr, nc, balance):
                        dp[(r, c, balance)] = True
                        return True

            dp[(r, c, balance)] = False
            return False

        return dfs(0, 0, 0)