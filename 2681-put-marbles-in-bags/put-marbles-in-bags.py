class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:

        maxHeap = []
        minHeap = []
        n = len(weights)

        for i in range(n - 1):
            cost = weights[i] +  weights[i + 1]
            heapq.heappush(maxHeap,-cost)
            heapq.heappush(minHeap,cost)


        min_ans = 0
        max_ans = 0

        i = 0

        while i < k - 1:
            maxCost = -heapq.heappop(maxHeap)
            minCost = heapq.heappop(minHeap)
            max_ans += maxCost
            min_ans += minCost

            i += 1

        
        return max_ans - min_ans


        


