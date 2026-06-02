class Solution:
    def findIntegers(self, n: int) -> int:

        bin_n = (bin(n)[2:])
        L = len(bin_n)

        dp = {}
        def solve(index,tight,valid,prev):

            if index == L:
                return 1

            if (index,tight,valid,prev + 1)  in dp:
                return dp[(index,tight,valid,prev + 1)]
                

            limit = int(bin_n[index]) if tight else 1

            ans = 0
            
            for d in range(limit + 1):
                ntight = tight and (d==limit)
                nvalid = valid or (d != 0)
                nprev  = d if nvalid else prev
                if d == 1 and prev == 1:
                    continue

                ans += solve(index+ 1,ntight,nvalid,nprev)

            dp[(index,tight,valid,prev + 1)] = ans
            return ans

        return solve(0,1,False,-1)

            

            



        
        