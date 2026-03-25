class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:

        rows = len(grid)
        cols = len(grid[0])

        soR = [0] * rows
        soC = [0] * cols

        for r in range(rows):
            soR[r] = sum(grid[r])
        
        

        
        for c in range(cols):
            for r in range(rows):
                soC[c] += grid[r][c]

        
        sumR = sum(soR)
        sumC = sum(soC)

        total = 0

        

        if sumR % 2 == 0:

            for el in soR:
                total += el
                if total == (sumR) / 2:
                    return True

        total = 0
        if sumC % 2 == 0:
            for el in soC:
                total += el
                if total == (sumC) / 2:
                    return True

        return False


            


        