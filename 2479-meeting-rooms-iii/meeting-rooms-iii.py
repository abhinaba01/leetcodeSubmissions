class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        

        avlRoom = []
        actRoom = []
        room = [0] * n
        ans = -1
        maxRoom = -1

        meetings.sort()

        for i in range(n):
            heapq.heappush(avlRoom,i)

       
        
        for start,end in meetings:

            while actRoom and start >= actRoom[0][0]:
                freeTime , no = heapq.heappop(actRoom)
                heapq.heappush(avlRoom,no)

            if not avlRoom:
                freeTime ,no = heapq.heappop(actRoom)
                heapq.heappush(actRoom,(freeTime + end - start,no))
                
                room[no] += 1

            else:
                roomNo = heapq.heappop(avlRoom)
                room[roomNo] += 1
                heapq.heappush(actRoom,(end,roomNo))

        for i in range(n):
            if room[i] > maxRoom:
                maxRoom = room[i]
                ans = i
          
        return ans

