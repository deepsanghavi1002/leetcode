# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        pval = p.val
        qval = q.val
        
        
        node = root
        while node:
            
            parentval = node.val
            
            if pval > parentval and qval > parentval:
                
                node = node.right 
                
            elif pval < parentval and qval < parentval:
                
                node = node.left 
                
            else:
                return node