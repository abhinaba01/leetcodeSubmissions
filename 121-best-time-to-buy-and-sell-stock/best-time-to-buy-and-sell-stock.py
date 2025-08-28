class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        minPrice = float("inf")
        maxProfit = float("-inf")

        for i in range(n):
            if prices[i] < minPrice:
                minPrice = prices[i]
            
            currProfit = prices[i] - minPrice
            maxProfit = max(currProfit,maxProfit)
        
        return maxProfit




