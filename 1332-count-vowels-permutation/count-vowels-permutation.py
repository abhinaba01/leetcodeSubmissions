class Solution:
    def countVowelPermutation(self, n: int) -> int:

        dp = [[-1] * 6 for _ in range(n+1)]
        MOD = 10 ** 9 + 7

        def rec(i,prev):

            if prev == "":
                return (rec(i+1,"a") + rec(i+1,"e") + rec(i+1,"i") + rec(i+1,"o") + rec(i+1,"u")) % MOD
            if prev == "a":
                ch = 1
            if prev == "e":
                ch = 2
            if prev == "i":
                ch = 3
            if prev == "o":
                ch = 4
            if prev == "u":
                ch = 5

            if dp[i][ch] != -1:
                return dp[i][ch]

            if i == n:
                return 1
            if prev == "a":
                ans =  rec(i+1,"e") % MOD
            if prev == "e":
                ans =  (rec(i+1,"a") + rec(i+1,"i") ) % MOD
            if prev == "i":
                ans =  (rec(i+1,"a") + rec(i+1,"e") + rec(i+1,"o") + rec(i+1,"u")) % MOD
            if prev == "o":
                ans = (rec(i+1,"i") + rec(i+1,"u")) % MOD
            if prev == "u":
                ans =  (rec(i+1,"a")) % MOD
            
            dp[i][ch] = ans
            return ans
            
          
            

        
        return rec(0,"")
            


        