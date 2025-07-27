class Solution:
    def minCut(self, s: str) -> int:

        n = len(s)

        dp = [-1 for i in range(n+1)]

        def isPalindrome(s:str):
            return s == s[::-1]

        def dfs(i):

            if i == n: 
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            minLength = float("inf")
            for k in range(i,n):
                if isPalindrome(s[i:k+1]):
                    cost =  1 + dfs(k+1)
                    minLength = min(minLength,cost)
                    dp[i] = minLength
            return dp[i]
        return dfs(0) - 1
            




        