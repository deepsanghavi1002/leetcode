"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.visited = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        if node in self.visited:
            return self.visited[node]
        else:
            clone_node = Node(val = node.val, neighbors = [])
            self.visited[node] = clone_node
            if node.neighbors:
                clone_node.neighbors = [self.cloneGraph(n)  for n in node.neighbors]
            return clone_node
        