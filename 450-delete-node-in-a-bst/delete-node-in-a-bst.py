# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None

        def findSuccessor(node):
            successor = None
            
            while node:
            
                successor = node
                node = node.left
            return successor


        if root.val > key:
            root.left = self.deleteNode(root.left,key)
        elif root.val < key:
            root.right = self.deleteNode(root.right,key)
        else:
            if not root.left and not root.right:
                return None
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            else:
                succ = findSuccessor(root.right)
                root.val = succ.val
                root.right = self.deleteNode(root.right, succ.val)
        
        return root

            
        