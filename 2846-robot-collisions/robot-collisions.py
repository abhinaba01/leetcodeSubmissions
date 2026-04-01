class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        
        N = len(positions)
        minHeap = []

        ans = []

        for i in range(N):
            
            heapq.heappush(minHeap,(positions[i],healths[i],directions[i],i))

        order = []

        start = 0

        while minHeap:
            
            pos,health,directions,index = heapq.heappop(minHeap)
            order.append([health,directions,pos,index])


        stack = []
        top = -1
        start = 0

        for health,direction,pos,index in order:

            exist = 0

           
            if not stack or stack[top][1] == direction or stack[top][1] == 'L' and direction == 'R':
                stack.append([health,direction,pos,index])
                top += 1

            else:
                
                while stack and stack[top][1] == 'R' and direction == 'L':
                    if stack[top][0] > health:
                        stack[top][0] -= 1
                        exist = 0
                        break

                    if stack[top][0] == health:
                        
                        
                        stack.pop(top)
                        top -= 1
                        exist = 0
                        
                        break
                    
                    else:
                        top -= 1
                        stack.pop()
                        health -= 1
                        exist = 1

                if exist:
                    stack.append([health,direction,pos,index])
                    top += 1
      
        sorted_stack = sorted(stack, key =lambda ep:ep[3])
        
        for health , direction,pos,index in sorted_stack:
            ans.append(health)

        
        return ans
                





