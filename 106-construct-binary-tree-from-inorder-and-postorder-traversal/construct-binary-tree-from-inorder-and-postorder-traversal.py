# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def findRoot(postO,inO):
            if not postO or not inO:
                return

            root = TreeNode(postO[-1])
            postO.pop()
           

            ind = inO.index(root.val)
           
            
            left = inO[:ind]
            right = inO[ind+1:]
            
            root.right = findRoot(postO,right)
            root.left = findRoot(postO,left)

            return root
        
        return findRoot(postorder,inorder)
        