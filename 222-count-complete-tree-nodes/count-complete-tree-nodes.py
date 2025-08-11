# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:

        def heightLeft(node):
            h = 0

            while node:
                h += 1
                node = node.left
            
            return h

        def heightRight(node):
            h = 0

            while node:
                h += 1
                node = node.right
            
            return h

        print(heightLeft(root))

                

        def count(node):

            if not node:
                return 0
            
            left_height = heightLeft(node) 
            right_height = heightRight(node) 

            if left_height == right_height:
                return  (2 ** left_height) - 1
            
            else:
                return 1 + count(node.left) + count(node.right)
        
        return count(root)
            
        
        

            


   


        

             







        