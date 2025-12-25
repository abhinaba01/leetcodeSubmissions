class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        @cache
        def count(i,j):

            if i >= m:
                return 0
            if j >= n:
                return 0
            
            if obstacleGrid[i][j] == 1:
                return 0

            if i == m -1 and j == n -1:
                return 1

           
            
            else:

                return count(i+1,j) + count(i,j+1)
        
        return count(0,0)
        