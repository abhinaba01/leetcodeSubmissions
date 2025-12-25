class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        n = len(locations)

        MOD = 10 ** 9 + 7

        @cache
        def countWays(ind,left):


            ans = 0
         
            if left < 0:
                return 0

            if left == 0:
                if ind != finish:
                    return 0
                return 1

            if ind == finish:
                ans = 1
        

            for i  in range(n):
                if i != ind:
                   
                    
                    ans = ( ans + countWays(i,left - abs(locations[ind] - locations[i]))) % MOD
                   
            return ans
        
        return countWays(start,fuel)


        