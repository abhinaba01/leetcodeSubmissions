class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:

        n = 18
        row = len(grid)
        col = len(grid[0])
        res = 0
        x = 0

        valid = [[True] * col for _ in range(row)]

        for i in range(n-1,-1 ,-1):

            

           

            arr = [False] * row
            

            for r in range(row):
                for c in range(col):
                    if valid[r][c] == False:
                        continue

                    num = grid[r][c]
                
                    if  (num & (1 << i)) == 0:
                       arr[r] = True
                       break
                   

            if False in arr:
                res += (2 ** (i))
            else:
                for r in range(row):
                    for c in range(col):
                        if valid[r][c] and (grid[r][c]  & (1 << i)) != 0:
                            valid[r][c] = False

                

        return res
                
                


                





        

        