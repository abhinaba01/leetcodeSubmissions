class Solution:
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:

        n = len(s)

        prefix = [0]*(n+1)

        for i in range(n):
            prefix[i+1] = prefix[i] + int(s[i])

        
        def calCost(l,r):

            length = r-l+1
            ones = prefix[r+1] - prefix[l]

            if ones == 0:
                segCost = flatCost
            else:
                segCost = length * ones * encCost

            if length % 2 == 1:
                return segCost

            mid = (l+r)//2

            splitCost = calCost(l,mid) + calCost(mid+1,r)

            return min(segCost, splitCost)

        return calCost(0,n-1)