# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        main_iter = []

        for el in lists:
            iter = []
            while el:
                iter.append(el.val)
                el = el.next
            main_iter.append(iter)

        
        ans = list(heapq.merge(*main_iter))
        dummyNode = ListNode(0)
        temp = dummyNode

        for el in ans:
            temp.next = ListNode(el)
            temp = temp.next
        
        return dummyNode.next

            
                