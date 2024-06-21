# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        d = defaultdict(list)
        queue = deque([(root,0)])
        
        while queue:
            node, column = queue.popleft()
            if node != None:
                d[column].append(node.val)
            
            
                queue.append((node.left, column-1))
                
            
                queue.append((node.right, column+1))
                
        res = []
        for key in sorted(d.keys()):
            print(d[key])
            res.append(d[key])
            
        return res
        
            
            
            
                
                
