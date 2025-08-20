# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        count = 0
        temp = head
        while temp:
            temp = temp.next
            count += 1

        if n == count:
            return head.next

        pos = 0
        temp = head
       
        while pos < count - n - 1:
            temp = temp.next
            pos += 1
        
        temp.next = temp.next.next
        return head



        