from functools import cache
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        n = len(s)

        @cache

        def dfs(i,j):

            if i > j:
                return 0

            

            if s[i] == s[j]:
                if i == j:
                    ans = 1
                else:
                    ans = 2 + dfs(i + 1 , j - 1)

            else:

                ans = max(dfs(i+1,j),dfs(i,j-1))

            
            return ans


        
        return dfs(0,n-1)

