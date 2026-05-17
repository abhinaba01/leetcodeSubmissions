class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        P = 911383323
        MOD = 10 ** 18 + 3

        h = 0
        POW = pow(P , 9 , MOD)

        freq = defaultdict(int)
        res = set()

        n = len(s)

        if n < 10:
            return []
        

        for i in range(10):

            h = (h * P + ord(s[i])) % MOD
        
        freq[h] += 1

        for j in range(10,n):

            h = (h - ord(s[j-10]) * POW) % MOD
            h = (h * P + ord(s[j])) % MOD

            freq[h] += 1
            

            if freq[h] > 1:
                res.add(s[j-9:j+1])
            

        
        return list(res)


        

            
        