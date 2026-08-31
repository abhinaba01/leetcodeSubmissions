# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        INF = 10 ** 18

        prev = head
        curr = head
        nxt = curr.next

        pos = []
        idx = 0

        while curr.next.next:

           
            prev = curr
            curr = curr.next
            idx += 1
            
            nxt = nxt.next


            print(prev.val ,curr.val , nxt.val)

            if prev.val < curr.val and curr.val > nxt.val:
                pos.append(idx)

            elif prev.val > curr.val and curr.val < nxt.val:
                pos.append(idx)

        if len(pos) < 2:
            return [-1,-1]

        minDistance = INF
        
        for i in range(1,len(pos)):

            diff = pos[i] - pos[i - 1]
            minDistance = min(minDistance , diff)


        maxDistance = pos[-1] - pos[0]

        return [minDistance , maxDistance]

        
        
        