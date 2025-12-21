class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        subsetSum = total_sum // 2
        n = len(nums)

        dp = [[-1  for _ in range(total_sum + 1)] for _ in range(n+1)]

        print(sum(nums),n+1)
        
        def dfs(i,total):
           
            if total == subsetSum:
                return 1
            
            if total > subsetSum:
                return 0
            
            if i >= n and total < subsetSum :
                return 0
            

            if dp[i][total] != -1:
                return dp[i][total] 

           
          
            if  dfs(i+1,total+nums[i])  == 1 or  dfs(i+1,total) == 1:
                dp[i][total] = 1
                return 1

            dp[i][total] = 0   
            return 0
            
            
        
        return True if dfs(0,0) == 1 else False
              

