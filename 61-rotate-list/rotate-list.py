# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head:
            return None 

        if not head.next or k == 0:
            return head 

        temp = head
        count = 0
        l = 0

        while temp:
            temp = temp.next
            l += 1
        
        k = k % l
        if k == 0:
            return head

        temp = head
        
        while temp:
            temp = temp.next
            count += 1
            if count == k:
                break
        
        start = head
        while temp.next:
            temp = temp.next
            start = start.next
        
        new_start = start.next      
        temp.next = head
        start.next = None
        return new_start

        