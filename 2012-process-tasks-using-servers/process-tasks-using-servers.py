class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:

        avlHeap = []
        actHeap = []
        
        m = len(tasks)
        n = len(servers)
        arr = [0] * m
        
        for i in range(n):
            heapq.heappush(avlHeap,(servers[i],i))

        
    

        for i in range(m):

            while actHeap and actHeap[0][0] <= i:
                freeTime , weight ,index = heapq.heappop(actHeap)
                heapq.heappush(avlHeap,(weight,index))

            if avlHeap:
                server , pos = heapq.heappop(avlHeap)
                arr[i] =  pos
                heapq.heappush(actHeap,(i + tasks[i],server,pos))
            else:
                freeTime,weight , index =  heapq.heappop(actHeap)
                arr[i] = index
                heapq.heappush(actHeap, (freeTime + tasks[i], weight, index))
               

        
        return arr



        