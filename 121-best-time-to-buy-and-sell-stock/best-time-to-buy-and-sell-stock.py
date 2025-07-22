class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        maxProfit = 0
        minPrice = float("inf")
        n = len(prices)
        for i in range(n):
            if prices[i] < minPrice: 
                minPrice = prices[i]
            
            currentProfit = prices[i] - minPrice
            if currentProfit > maxProfit:
                maxProfit = currentProfit

        return maxProfit


          
