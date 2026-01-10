class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:

        n = len(nums1)

        INF = 10**18
        dp = [INF] * (1 << n)
        dp[0] = 0 

        for mask in range(1 << n):
            k = bin(mask).count("1") 
            if k >= n:
                continue

            for i in range(n):
                if not (mask & (1 << i)):
                    new_mask = mask | ( 1<< i)
                    dp[new_mask] = min(dp[new_mask],dp[mask] + (nums1[k] ^ nums2[i]))

        
        answer = dp[(1 << n) - 1]
        return answer






        

      