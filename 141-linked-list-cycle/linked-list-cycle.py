# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        temp = head
        dictMap = {}
        while temp:
            if temp in dictMap:
                return True
            dictMap[temp] = dictMap.get(temp,0) + 1
            temp = temp.next
        
        



            


        