# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        ll = []
        
        while head:
            ll.append(head.val)  
            head = head.next
        
        ll.sort()

        head = ListNode(ll[0])
        current = head

        for val in ll[1:]:

            current.next = ListNode(val)
            current = current.next

        return head
            
        

        