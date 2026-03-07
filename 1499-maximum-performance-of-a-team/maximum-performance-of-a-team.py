class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:

        engineers = [0] * n

        for i in range(n):
            engineers[i] = efficiency[i] , speed[i]

        engineers.sort(reverse = True)

        
        minHeap = []
        ans = -math.inf
        sumS = 0
        MOD = 10 ** 9 + 7

        for e ,s in engineers:
            
            heapq.heappush(minHeap , s)
            sumS += s

         

            if len(minHeap) > k:
                sp = heapq.heappop(minHeap)
                sumS -= sp

            if len(minHeap) <= k:
               
                ans = max(ans , (sumS * e)  )


        return ans % MOD

        
            


    

        

        

        


        
        