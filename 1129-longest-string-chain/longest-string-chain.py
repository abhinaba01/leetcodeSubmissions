class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        n = len(words)
        words.sort(key = len)

        dp = [[-1 for i in range(n + 1)] for _ in range(n)]


      
        def isPredecessor(ind, prev):
            shorter = words[prev]
            longer = words[ind]
            if len(longer) != len(shorter) + 1:
                return False

            i = j = 0
            mismatch = 0

            while i < len(shorter) and j < len(longer):
                if shorter[i] == longer[j]:
                    i += 1
                    j += 1
                else:
                    mismatch += 1
                    j += 1
                    if mismatch > 1:
                        return False

            return True

            

        def dfs(ind,prev):
            
            if ind == n:
                return 0

            if dp[ind][prev + 1] != -1:
                return dp[ind][prev + 1]
            
            taken = 0
            if prev == -1 or  isPredecessor(ind,prev):
                taken = 1 + dfs(ind +1,ind)
            
            not_taken = dfs(ind +1,prev)

            dp[ind][prev + 1] = max(taken,not_taken)
            return dp[ind][prev + 1]


        return dfs(0,-1)

        