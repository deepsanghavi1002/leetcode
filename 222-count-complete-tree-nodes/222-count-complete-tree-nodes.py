# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lh(self, node, height):
        if not node:
            return height
        return self.lh(node.left,height+1)
        
    def rh(self, node, height):
        if not node:
            return height
        return self.rh(node.right,height+1)
            
            
    def countNodes(self, root: Optional[TreeNode]) -> int:
        left = self.lh(root,0)
        right = self.rh(root,0)
        
        if left == right:
            return (2 ** left) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        
        
        