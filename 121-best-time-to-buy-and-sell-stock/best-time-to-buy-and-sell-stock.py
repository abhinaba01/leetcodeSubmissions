class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        maxProfit = 0
        minPrice = float("inf")
        n = len(prices)
        for i in range(n):
            minPrice = min(prices[i], minPrice)
            maxProfit = max(maxProfit,prices[i] - minPrice)

        return maxProfit


          
