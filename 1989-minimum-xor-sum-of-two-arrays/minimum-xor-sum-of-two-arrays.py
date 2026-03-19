class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:

        n = len(nums1)

        dp = [[-1] * n for _ in range(1 << n)]

        def solve(i,mask):

            if i == n:
                return 0

            ans = float("inf")
            
            if dp[mask][i] != -1:
                return dp[mask][i]



            
            for j in range(n):

                if not mask & (1 << j):
                    
                    ans = min(ans,solve(i+1,mask | (1 << j)) + (nums1[i] ^ nums2[j]))

            dp[mask][i] = ans  
            return ans

        return solve(0,0)


