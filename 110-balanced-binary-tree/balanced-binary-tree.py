# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        a = True
        def dfs(node):
            nonlocal a

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            n =  abs(left - right)

            if n > 1:
                a = False
            
            return max(left,right) + 1
                

        dfs(root)  
        if not a:
            return False
        else:
            return True






        