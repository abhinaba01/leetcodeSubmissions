class Solution:
    def minInsertions(self, s: str) -> int:

        n = len(s)

        @cache
        def lps(i,j):

            if i == j:
                return 1
            
            if i > j:
                return 0
            
            if s[i] == s[j]:
                return 2 + lps(i + 1 , j - 1)

            else:
                return max(lps(i + 1 , j) , lps(i , j - 1))



        
        x = lps(0,n - 1)

        return n - x