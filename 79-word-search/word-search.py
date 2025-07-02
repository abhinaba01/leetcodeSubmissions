class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        ROWS = len(board)
        COLS = len(board[0])
        visited = []


        def dfs(i,j,k):
            
            if k == len(word):
                return True

            if (i< 0 or i >= ROWS or j<0 or j >= COLS or word[k] != board[i][j] or [i,j] in visited):
                return False

            visited.append([i,j])
         

            res = dfs(i+1,j,k+1) or  dfs(i-1,j,k+1) or  dfs(i,j+1,k+1) or  dfs(i,j-1,k+1)

            visited.remove([i,j])
         
            return res

        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True

        return False
        
             
               
        
            
                


        