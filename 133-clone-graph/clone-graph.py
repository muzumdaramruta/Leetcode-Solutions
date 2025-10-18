"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        copied = {}

        def dfs(curr):
            if curr in copied:
                return copied[curr]
            clone = Node(curr.val, [])
            copied[curr] = clone

            for neighbor in curr.neighbors:
                clone_neighbors = dfs(neighbor)
                clone.neighbors.append(clone_neighbors)
            return clone
        
        return dfs(node)