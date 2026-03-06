class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:

        maxHeap = []
        stations.append([target,0])

 

        c = 0
        prev_pos = 0
        
    
        for pos , fuel in stations:
            
            while startFuel - (pos - prev_pos) < 0:
                if maxHeap:
                    f  =  heapq.heappop(maxHeap)
                    f = -f
                  
                    startFuel += f
                    c += 1
                else:
                    return -1
                    
            heapq.heappush(maxHeap,-fuel)
            startFuel -= (pos - prev_pos)

            prev_pos = pos

        return c
