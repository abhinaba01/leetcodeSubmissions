class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        m = len(image)
        n = len(image[0])

        
        vis = [[False for i in range(n)] for _ in range(m)]
        prev_color = image[sr][sc]

        if prev_color == color:
            return image


        def dfs(i,j):

            if j < 0 or j > n-1 or i < 0 or i > m - 1:
                return
         
            if vis[i][j] or image[i][j] != prev_color:
                return

            vis[i][j] = True
            image[i][j] = color
            

            
            dfs(i,j-1)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i+1,j)

            

        dfs(sr,sc)
        return image

        



        