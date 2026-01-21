class Solution:
    def reorganizeString(self, s: str) -> str:

        freq = Counter(s)
        s1 = ""

        maxHeap = []

        for ch, f in freq.items():
            heapq.heappush(maxHeap, (-f, ch))

        l = len(maxHeap)

        while maxHeap:

            cycle = 2 
            temp = []

            while cycle > 0 and maxHeap:
                
                cnt , ch = heapq.heappop(maxHeap)
                if cnt + 1 < 0:
                    temp.append((cnt+1,ch))
                s1 += ch

                cycle -= 1
                l -= 1

            for f,item in temp:
                heapq.heappush(maxHeap,(f,item))

            
            if len(maxHeap) == 1:
              
                f ,item = heapq.heappop(maxHeap)
                if f < -1:
                    return ""

                else:
                    heapq.heappush(maxHeap,(f,item))

        
        return s1
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            
                

            
                
    












        