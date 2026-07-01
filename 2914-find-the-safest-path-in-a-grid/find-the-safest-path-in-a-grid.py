class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        if grid[0][0] == 1:
            return 0
        
        INF = 10 ** 18

        dist = [[INF] * cols for _ in range(rows)]

        pq = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    pq.append((r,c))


        
      
        dire = [(0,1),(0,-1),(1,0),(-1,0)]

        while pq:
            
            r, c = pq.popleft()

        
           

            for dr , dc in dire:
                nr = r + dr
                nc = c + dc

                if not(0 <= nr < rows and 0 <= nc < cols):
                    continue
                
                if dist[nr][nc] != INF:
                    continue

                dist[nr][nc] = dist[r][c] + 1
                pq.append((nr,nc))


        def isPossible(val):

            pq = deque([(0,0)])
            visited = [[False] * cols for _ in range(rows)]
            visited[0][0] = True

            if dist[0][0] < val:
                return False

            while pq:

                r , c = pq.popleft()

                if r == rows - 1 and c == cols - 1:
                    return True

                
                for dr , dc in dire:
                    nr = r + dr
                    nc = c + dc

                    if not(0 <= nr < rows and 0 <= nc < cols):
                        continue
                    
                    if visited[nr][nc]:
                        continue

                    if dist[nr][nc] < val:
                        continue
                    
                    visited[nr][nc] = True
                    pq.append((nr,nc))

            
            return False




        low , high = 0 , rows + cols + 1
        ans = 0

        while low <= high:

            mid = (low + high) // 2

            if isPossible(mid):
                ans = mid
                low = mid  + 1
            else:
                high = mid - 1

        


        return ans
            
                

                






        