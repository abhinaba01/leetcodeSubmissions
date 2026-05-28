class Solution:
    def minCost(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        directions = {(-1,0):4,(1,0):3,(0,1):1,(0,-1):2}

        pq = deque([(0,0)])

        INF = math.inf

        dist = [[INF] * cols for _ in range(rows)]

        dist[0][0] = 0

        while pq:

            r , c = pq.popleft()

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if (0 <= nr < rows and 0<= nc < cols):

                    if directions[(dr,dc)] == grid[r][c]:
                        cost = 0
                    else:
                        cost = 1
                    
                    new_dist = dist[r][c] + cost

                    if new_dist < dist[nr][nc]:
                        dist[nr][nc] = new_dist

                        if cost == 0:
                            pq.appendleft([nr,nc])
                        else:
                            pq.append([nr,nc])


        return dist[-1][-1]



    


        