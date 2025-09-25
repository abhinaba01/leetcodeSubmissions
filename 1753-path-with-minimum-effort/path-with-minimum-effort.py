class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        visited = set()
        neighbors = [(0,1),(0,-1),(-1,0),(1,0)]
        rows = len(heights)
        cols = len(heights[0])

        def bfs(r,c,k,visited):
            if r == rows -1 and c == cols - 1:
                return True
            if (r,c) in visited:
                return False
            visited.add((r,c)) 
            neighbors = [(0,1),(0,-1),(-1,0),(1,0)]
            for dr,dc in neighbors:
                if min(r+dr,c+dc) < 0 or r + dr == rows or c + dc == cols:
                    continue
                if (r+dr,c+dc) not in visited:
                    if abs(heights[r+dr][c+dc] - heights[r][c]) <= k:
                        if bfs(r+dr,c+dc,k,visited):
                            return True
                        
            return False

        
        low = 0
        high = max(
    (abs(heights[r][c] - heights[r+dr][c+dc])
     for r in range(rows)
     for c in range(cols)
     for dr, dc in neighbors
     if 0 <= r+dr < rows and 0 <= c+dc < cols),
    default=0
)
       

        while low < high:
            mid = (low + high) // 2
            visited = set()
            if bfs(0,0,mid,visited):
                high = mid
            else:
                low = mid + 1
        return low


        