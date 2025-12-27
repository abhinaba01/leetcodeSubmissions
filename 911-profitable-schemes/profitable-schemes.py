class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:

        l = len(group)
        MOD = 10 ** 9 + 7

        @cache
        def solve(k,i,totalProfit):

            if i >= l:
                if totalProfit >= minProfit:
                    return 1
                else:
                    return 0
           
            cnt = 0

           

            if k - group[i] >= 0:
                cnt = (cnt + solve(k-group[i],i+1,min(minProfit,totalProfit + profit[i]))) % MOD
                
            cnt = (cnt + solve(k,i+1,totalProfit)) % MOD

            return cnt

        return solve(n,0,0)

        