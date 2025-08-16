# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node):

            if not node:
                return
            
            if node == p:
                return p
            if node == q:
                return q

            left = dfs(node.left)
            right = dfs(node.right)
            

            if not left and not right:
                return
            
            if left:
                if not right:
                    return left
                else:
                    return node
            
            if right:
                if not left:
                    return right
                else:
                    return node
            
        return dfs(root)
                
                