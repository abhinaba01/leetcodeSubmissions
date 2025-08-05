# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        result = []
        if not root:
            return result
        
        queue = [root]
        c = 0

        while queue:

            
            level = len(queue)
            path = []

            for i in range(level):

                node = queue.pop(0)
                path.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if (c%2) != 0:
                result.append(path[::-1])
            else:
                result.append(path)

            c += 1
        
        return result

