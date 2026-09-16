class Solution:
    def numberOfSets(self, n: int, k: int) -> int:

        MIN = k + 1
        MAX = min(2 * k , n)
        total = 0
        MOD = 10 ** 9 + 7

        for el in range(MIN , MAX + 1):
            ways = math.comb(n,el) * math.comb(k - 1, 2 * k - el)
            total = (total +  ways) % MOD
        
        return total % MOD



        

        
        