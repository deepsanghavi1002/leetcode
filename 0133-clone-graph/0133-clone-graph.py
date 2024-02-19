"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
class Solution:
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}
        dq = deque()
        
        if node == None:
            return None
        dq.append(node)
        visited[node] = Node(node.val, [])
        while dq:
            currNode = dq.popleft()
            for neighbor in currNode.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    dq.append(neighbor)
                visited[currNode].neighbors.append(visited[neighbor])
        return visited[node]
        