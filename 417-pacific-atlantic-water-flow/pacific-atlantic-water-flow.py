class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows = len(heights)
        cols = len(heights[0])

        if not heights:
            return []
        
        pacific = set()
        atlantic = set()
        

        def dfs(r,c,visited):
            visited.add((r,c))
            nei = [(-1,0),(0,1),(1,0),(0,-1)]

            for dr,dc in nei:

                if min(r+dr,c+dc) < 0  or r + dr == rows or c + dc == cols or (r+dr,c+dc) in visited:
                    continue
                
                if heights[r+dr][c+dc] >= heights[r][c]:
                    dfs(r+dr,c+dc,visited)
                   

        for r in range(rows):
            dfs(r,0,pacific)
        for r in range(rows):
            dfs(r,cols-1,atlantic)
        for c in range(cols):
            dfs(0,c,pacific)
        for c in range(cols):
            dfs(rows-1,c,atlantic)

        return list(pacific & atlantic)
              

       
       
      
     

        






        