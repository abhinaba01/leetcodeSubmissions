# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        path = []
        def preOrder(node,path):
        
            if not node:
                return 
            
            else:
                path.append(node.val)
                
                preOrder(node.left,path)

                preOrder(node.right,path)

                return path
            
        preOrder(root,path)
        return path

            


        