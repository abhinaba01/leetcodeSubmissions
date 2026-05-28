class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        pq = deque([(0,0)])

        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        
        INF = math.inf

        dist = [[INF] * cols for _ in range(rows)]
        dist[0][0] = 0

        while pq:

            r , c = pq.popleft()

            for dr , dc in directions:
                
                nr = r + dr 
                nc = c + dc  

                if (0 <= nr < rows and 0 <=nc < cols):

                    if grid[nr][nc] == 1:
                        
                        if dist[nr][nc] >  dist[r][c] + 1:
                            dist[nr][nc] = dist[r][c] + 1
                            pq.append([nr,nc])
                    else:
                        if dist[nr][nc] > dist[r][c]:
                            dist[nr][nc] = dist[r][c] 

                            pq.appendleft([nr,nc])

               
        
        return dist[rows - 1][cols - 1]



    
                    
        