class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:

        
        n = len(energy)
        dp = [float("-inf")] * n
        
        def dfs(i):
            
            if dp[i] != float("-inf"):
                return dp[i]
            
            
            if i + k < n:
                dp[i] = dfs(i+k) + energy[i]
            else:
                dp[i] = energy[i]

            return dp[i]
        
        for i in range(n):
            dfs(i)

        return max(dp)

        

                

   