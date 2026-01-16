class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        r = len(mat)
        c = len(mat[0])


        for i in range(r):
            for j in range(c):
                top = -1 if i <= 0 else mat[i-1][j]
                bottom = -1 if i >= r - 1 else mat[i+1][j]
                left = -1 if j <= 0 else mat[i][j-1]
                right = -1 if j >= c - 1 else mat[i][j+1]

                if mat[i][j] > left and mat[i][j] > right and mat[i][j] > top and mat[i][j] > bottom:
                    return [i,j]