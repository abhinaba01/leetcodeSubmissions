class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfit = 0
        minPrice = float("inf")
        n = len(prices)

        for i in range(n):
            minPrice = min(minPrice,prices[i])
           
            maxProfit = max((prices[i] - minPrice) , maxProfit)
        
        return maxProfit
        


        