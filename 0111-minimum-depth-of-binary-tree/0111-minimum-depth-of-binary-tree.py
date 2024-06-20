# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
            
        queue = [root]
        
        counter = 1
        while queue:
            
            next_level = []
            for node in queue:
                if node.left == None and node.right == None:
                    return counter
                if node.left != None:
                    next_level.append(node.left)
                if node.right != None:
                    next_level.append(node.right)
                
            queue = next_level
            counter += 1
                
                
        return counter
                
                
            
            
        