class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        dp = defaultdict(int)
        n = len(arr)
       

        
        for i in range(n):
        
            dp[arr[i]] = dp[arr[i]-difference] + 1 
        
        return max(dp.values())
