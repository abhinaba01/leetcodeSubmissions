class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        rows , cols = len(grid) , len(grid[0])

        pq = deque([(0,0,1)])

        INF = float("inf")
        ans = INF
        visited = set()

        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1
        

        while pq:

            r , c , steps = pq.popleft()

            if (r == rows - 1 and c == cols - 1):
                return steps
               
            dir = [(-1,0),(1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]

            for dr,dc in dir:

                nr = r + dr
                nc = c + dc


                if not ((0<= nr < rows) and (0<=nc <cols)):
                    continue
                
                if grid[nr][nc] == 1:
                    continue

                if (nr,nc) in visited:
                    continue

                visited.add((nr,nc))
                pq.append((nr,nc,steps + 1))

        return -1

        

                




        