class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        n = len(nums)
        min_heap = []

        for el in nums:
            heapq.heappush(min_heap,el)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return min_heap[0]