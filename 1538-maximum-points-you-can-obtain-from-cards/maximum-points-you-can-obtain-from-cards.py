class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        n = len(cardPoints)
        subLen = n - k
        l,r = 0, subLen

        sum_array = sum(cardPoints[0:subLen])
        total_sum = sum(cardPoints)
        minSum = sum_array

        
        while r < n:

            sum_array += (cardPoints[r] - cardPoints[l])
            minSum = min(minSum,sum_array)

            r += 1
            l += 1
        
        return total_sum - minSum


            



        