class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        nums = []
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                heapq.heappush_max(nums,matrix[r][c])

                if len(nums) > k:
                    heapq.heappop_max(nums)
        
        return heapq.heappop_max(nums)


        


        