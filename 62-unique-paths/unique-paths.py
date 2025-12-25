class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        @cache
        def count(i,j):

            if i >= m:
                return 0
            if j >= n:
                return 0

            if i == m -1 and j == n -1:
                return 1
            
            else:

                return count(i+1,j) + count(i,j+1)
        
        return count(0,0)
        