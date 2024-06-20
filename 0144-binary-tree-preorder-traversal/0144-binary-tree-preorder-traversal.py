# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        queue = [] 
        res = []
        if root == None:
            return []
        queue.append(root) 
        while len(queue) != 0:
            current = queue.pop()
            print(current.val)
            
            if current.right!= None:
                queue.append(current.right)
            if current.left!=None:
                queue.append(current.left)
            
                
            res.append(current.val)    
        return res