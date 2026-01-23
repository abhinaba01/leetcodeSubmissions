class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:

        n = len(heights)
        minHeap = []

        for i in range(n - 1):
        
            diff = heights[i+1] - heights[i]
            if diff > 0:
                heapq.heappush(minHeap,diff)
          
            if len(minHeap) > ladders:
                x = heapq.heappop(minHeap)
               
                if bricks >= x:
                    bricks -= x
                else:
                    return i
        return n - 1

  
              


        