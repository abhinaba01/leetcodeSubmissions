class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [[-1 for i in range(n + 1)] for _ in range(n)]

       
        def dfs(i,prev):

            if i == n:
                return 0
            
            if dp[i][prev + 1] != -1:
                return dp[i][prev + 1]


           
            

            if prev == -1:
                nprev = float("-inf")
            else:
                nprev = nums[prev]

            if nums[i] > nprev:
                dp[i][prev + 1] = max(dfs(i+1,i) + 1, dfs(i+1,prev))
            else:
                
                dp[i][prev + 1] = dfs(i+1,prev)
            return dp[i][prev + 1]

        return dfs(0,-1)

            

                


            
       

            




            

