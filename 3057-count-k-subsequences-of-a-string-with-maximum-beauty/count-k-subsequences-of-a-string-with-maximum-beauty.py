class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        
        MOD = 10**9 + 7

        freq = Counter(s)
        vals = sorted(freq.values(), reverse=True)

        if len(vals) < k:
            return 0

        threshold = vals[k-1]

        greater = sum(1 for v in vals if v > threshold)
        equal = sum(1 for v in vals if v == threshold)

        need = k - greater

        ans = 1

      
        for v in vals:
            if v > threshold:
                ans = (ans * v) % MOD

       
        ans = (ans * math.comb(equal, need)) % MOD
        ans = (ans * pow(threshold, need, MOD)) % MOD

        return ans