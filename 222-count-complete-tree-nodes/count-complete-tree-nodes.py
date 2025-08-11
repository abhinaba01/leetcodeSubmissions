# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        queue = [root]
        c  = 0
        
        while queue:
            
            node = queue.pop(0)
            if node:
                c += 1
                queue.append(node.left)
                queue.append(node.right)
        
        return c


        

             







        