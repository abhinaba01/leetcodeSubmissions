class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        maxHeap = []
        n = len(arr)
        for index in range(n):
            heapq.heappush_max(maxHeap,(abs(arr[index] - x),index))

            if len(maxHeap) > k:
                heapq.heappop_max(maxHeap)

        
        ans = [arr[i] for f,i in maxHeap]

      

        ans.sort()
        return ans
        



       