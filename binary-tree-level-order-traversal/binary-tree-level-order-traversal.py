# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        res = []
        current_level = [root]
        next_level = []
        while len(current_level) != 0:
            next_level = []
            this_level = []
            for node in current_level:
                
                this_level.append(node.val)
                
                if node.left != None: 
                    next_level.append(node.left)
                if node.right != None:
                    next_level.append(node.right)
            res.append(this_level)
            current_level = next_level
            
                
            
        return res
        
        