class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:

        arr = [[0] * n for _ in range(n)]

        diff =  [[0] * (n + 1)  for _ in range(n+1)]


        
        for r1,c1,r2,c2 in queries:
            diff[r1][c1] += 1
            diff[r2+1][c1] -= 1
            diff[r1][c2+1] -= 1
            diff[r2+1][c2+1] += 1


        
        prefixSum = 0  

        for r in range(n):
            for c in range(n):
                top = diff[r - 1][c] if r > 0 else 0
                left = diff[r][c - 1] if c > 0 else 0
                diag = diff[r - 1][c - 1] if r > 0 and c > 0 else 0

                diff[r][c] += top + left - diag

                arr[r][c] = diff[r][c]
                
        return arr
        
