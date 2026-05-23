

def maxSubArray(A: List[int]) -> int:
    
    curr = A[0] + A[1]
    ans = curr
    b = A[1]
    for x in A[2:]:
        curr = max(b + x, curr+x)
        ans = max(ans, curr)
        b = x
    return ans
        
class Solution:
    def maxScore(self, A: List[List[int]]) -> int:
        N,M = len(A), len(A[0])
        ans = -inf
        for x in A:
            ans = max(ans, maxSubArray(x))
                
        for x in zip(*A):
            ans = max(ans, maxSubArray(x))

        for i in range(N):
            for j in range(M):
                if i > 0 and i < N - 1:
                    if j > 0 and j < M - 1:
                        ans = max(ans, A[i][j])
        return ans