class Solution:
    def minCut(self, s: str) -> int:

        n = len(s)

        dp = [-1 for i in range(n+1)]

       

        
        is_pal = [[False] * n for _ in range(n)]

        for i in range(n):
            is_pal[i][i] = True  # single letters

        for i in range(n - 1):
            is_pal[i][i + 1] = (s[i] == s[i + 1])  # two-letter substrings

        for length in range(3, n + 1):  # substrings of length >= 3
            for i in range(n - length + 1):
                j = i + length - 1
                is_pal[i][j] = s[i] == s[j] and is_pal[i + 1][j - 1]

    
        def dfs(i):

            if i == n: 
                return 0
            
            if dp[i] != -1:
                return dp[i]
            
            minLength = float("inf")
            for k in range(i,n):
                if is_pal[i][k]:
                    cost =  1 + dfs(k+1)
                    minLength = min(minLength,cost)
                    dp[i] = minLength
            return dp[i]
        return dfs(0) - 1
            




        