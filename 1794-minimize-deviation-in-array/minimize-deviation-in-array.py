class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:

        n = len(nums)

        for i in range(n):
            if nums[i] % 2 != 0:
                nums[i] = nums[i] * 2

       
        maxHeap = []
        minNum = math.inf

        for num in nums:
            minNum = min(minNum,num)
            
            heapq.heappush(maxHeap,-num)

        deviation = math.inf

        
        
        
        while (-maxHeap[0]) % 2 == 0:
            maxEl = - heapq.heappop(maxHeap)
           
            maxEl = maxEl // 2
            minNum = min(minNum,maxEl)
          
            heapq.heappush(maxHeap,-maxEl)
            deviation = min(deviation,abs(minNum + maxHeap[0]))

        return deviation

        

        

            



        
        