class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:


        N = len(nums)

        l = 0
        ans = 0

        maxHeap = []
        minHeap = []
        
        for r in range(N):

            heapq.heappush(maxHeap,(-nums[r],r))
            heapq.heappush(minHeap,(nums[r],r))

            while True:



                while maxHeap[0][1] < l:
                    heapq.heappop(maxHeap)
                while minHeap[0][1] < l:
                    heapq.heappop(minHeap)
                
                if -maxHeap[0][0] - minHeap[0][0] <= limit :
                    break
              
                

                l += 1
               

            ans = max(ans,r - l + 1)
        
        return ans