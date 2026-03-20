from typing import List

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        
        n = len(tasks)
        N = 1 << n
        
        
        subset_sum = [0] * N
        
        for mask in range(N):
            for i in range(n):
                if mask & (1 << i):
                    subset_sum[mask] += tasks[i]
        
      
        valid = [False] * N
        for mask in range(N):
            if subset_sum[mask] <= sessionTime:
                valid[mask] = True
        
        
        dp = [float('inf')] * N
        dp[0] = 0
        
        for mask in range(1, N):
            
            sub = mask
            while sub:
                
                if valid[sub]:
                    dp[mask] = min(dp[mask], dp[mask ^ sub] + 1)
                
                sub = (sub - 1) & mask
        
        return dp[N - 1]