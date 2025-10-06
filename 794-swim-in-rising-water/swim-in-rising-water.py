class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])



        def swim(r,c,k,visited):

            if r == rows - 1 and c == cols - 1:
                return True
            
            visited.add((r,c))
           

            nei = [(-1,0),(1,0),(0,-1),(0,1)]

            for dr,dc in nei:
                nr,nc = r+dr,c+dc
                if not(0 <= nr < rows and 0 <= nc < cols) or  grid[nr][nc] > k or (nr,nc) in visited:
                    continue
                if swim(nr,nc,k,visited):
                    return True
            
            return False


        
        
        low,high = 0, (rows * rows)
        mid = 0
        ans = 0

        while low <= high:
            mid = (low + high)// 2
            if grid[0][0] <= mid and swim(0,0,mid,set()):
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
            
                
        return ans

                
        