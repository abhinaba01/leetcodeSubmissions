class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        n = len(cardPoints)
        windowLen = n - k
        l,r = 0, windowLen

        windowSum = sum(cardPoints[:windowLen])
        total_sum = sum(cardPoints)
        minSum = windowSum

        while r < n:

            windowSum += (cardPoints[r] - cardPoints[l])
            minSum = min(minSum,windowSum)

            r += 1
            l += 1
        
        return total_sum - minSum


        