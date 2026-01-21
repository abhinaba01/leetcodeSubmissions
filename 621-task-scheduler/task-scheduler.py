class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = Counter(tasks)

        time = 0 
      

        maxHeap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxHeap)

        while maxHeap:
            temp = []
            cycle = n + 1

            while cycle > 0 and maxHeap:
                cnt = heapq.heappop(maxHeap)
                if cnt + 1 < 0:
                    temp.append(cnt + 1)
                cycle -= 1
                time += 1

            if temp:
                for ch in temp:
                    heapq.heappush(maxHeap,ch)
            
            if maxHeap:
                time += cycle
            
        
        return time
        

    
        