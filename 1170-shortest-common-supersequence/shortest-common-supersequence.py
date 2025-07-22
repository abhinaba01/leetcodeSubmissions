class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        n, m = len(str1), len(str2)

        # Step 1: Fill LCS table
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Step 2: Backtrack to get LCS string
        i, j = n, m
        lcs = ""

        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                lcs = str1[i - 1] + lcs
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

        



         # Step 3: Build SCS from str1, str2, and lcs
        res = []
        i = j = 0
        for c in lcs:
            # Add unmatched characters from str1
            while i < len(str1) and str1[i] != c:
                res.append(str1[i])
                i += 1
            # Add unmatched characters from str2
            while j < len(str2) and str2[j] != c:
                res.append(str2[j])
                j += 1
            # Add the LCS character
            res.append(c)
            i += 1
            j += 1

        # Add remaining characters
        res.extend(str1[i:])
        res.extend(str2[j:])

        return ''.join(res)

        

      