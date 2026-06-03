# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:


        def dfs(node):
            
            if not node:
                return 0 , 0
            

            left_take , left_not_take = dfs(node.left)
            right_take , right_not_take = dfs(node.right) 

            node_take = left_not_take + right_not_take + node.val
            node_not_take = max(left_take,left_not_take) + max(right_take,right_not_take)

            return node_take,node_not_take

        return max(dfs(root))

            