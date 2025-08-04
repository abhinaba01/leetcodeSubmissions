# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    
        result = []

        if not root:
            return result
        
        queue = [root]
        
        while queue:

            path = []

            level = len(queue)

            for _ in range(level):
                node =  queue.pop(0)
                path.append(node.val)

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                
            result.append(path[-1])
        
        return result




    