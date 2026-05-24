
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:


        rows = len(grid)
        cols = len(grid[0])

        mask = 0

        cnt = 0

        q = deque()
        visited = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "@":
                    q.append((r,c,mask,0))
                    visited.add((r,c,mask))
                elif 'a' <= grid[r][c] <= 'z':
                    cnt += 1


        
        target = (1 << cnt) - 1

        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        while q:

            r , c , mask , steps = q.popleft()


            if mask == target:
                return steps

            for dr , dc in directions:

                new_mask = mask

                nr = r + dr
                nc = c + dc

                boundary_check = ( 0 <= nr < rows and 0<= nc < cols)

                if not boundary_check:
                    continue
                
                wall_check = (grid[nr][nc] == "#")

                if wall_check:
                    continue

                    
                
                if ('A' <= grid[nr][nc] <= 'Z'):

                    lock_no = ord(grid[nr][nc]) - ord('A')

                    if not (new_mask & (1 << lock_no)):
                        continue

                if ('a' <= grid[nr][nc] <= 'z'):
                    key_no = ord(grid[nr][nc]) - ord('a')

                    new_mask = new_mask | (1 << key_no)

                if (nr,nc,new_mask) in visited:
                    continue

                

                visited.add((nr,nc,new_mask))
                q.append((nr,nc,new_mask,steps + 1))

            
        
        return -1


        
        


                






        

    
