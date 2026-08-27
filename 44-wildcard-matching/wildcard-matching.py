class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)

       
        dp = [False] * (m + 1)
        dp[0] = True

      
        for j in range(1, m + 1):
            if p[j - 1] == '*':
                dp[j] = dp[j - 1]

        for i in range(1, n + 1):
            new_dp = [False] * (m + 1)

            for j in range(1, m + 1):
                if p[j - 1] == '*':
                   
                    new_dp[j] = new_dp[j - 1] or dp[j]

                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    new_dp[j] = dp[j - 1]

            dp = new_dp

        return dp[m]