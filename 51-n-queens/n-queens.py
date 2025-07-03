class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        nQueens = [["." for _ in range(n)] for _ in range(n)]
        ans = []

        def isSafe(r,c):

            for i in range(c):
                if nQueens[r][i] == "Q":
                    return False
                

            rows = r
            cols = c
            while rows >= 0 and cols >= 0:
               
                if nQueens[rows][cols] == "Q":
                    return False
                rows-= 1
                cols-= 1

            rows = r
            cols = c
            while rows < n and cols >= 0:
               
                if nQueens[rows][cols] == "Q":
                    print(False)
                    return False
                
                rows+= 1
                cols-= 1

            return True


        def dfs(i):
            if i == n:
                board = []
                for row in nQueens:
                    board.append("".join(row))
                ans.append(board)
                
                return
            for r in range(n):
                if isSafe(r,i):
                    nQueens[r][i] = 'Q'
                    dfs(i+1)
                    nQueens[r][i] = "."

        dfs(0)
        return ans
            
            
            

        


        