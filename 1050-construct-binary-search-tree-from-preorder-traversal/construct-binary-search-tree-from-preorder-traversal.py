# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:

        inorder = sorted(preorder)
        print(inorder)

      
        def findRoot(preO,inO):
            if not preO or not inO:
                return

            root = TreeNode(preO[0])
            preO.pop(0)
           

            ind = inO.index(root.val)
           
            
            left = inO[:ind]
            right = inO[ind+1:]
            
            root.left = findRoot(preO,left)
            root.right = findRoot(preO,right)

            return root
        
        return findRoot(preorder,inorder)
        