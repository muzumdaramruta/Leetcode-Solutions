"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def dfs(self, node: 'Node', seen: dict[int, 'Node']) -> 'Node':
        root: 'Node' = Node(node.val)
        seen[node.val] = root
        for neighbor in node.neighbors:
            if neighbor.val not in seen: root.neighbors.append(self.dfs(neighbor, seen))
            else: root.neighbors.append(seen[neighbor.val])
        return root

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        seen: dict[int, 'Node'] = dict()
        return self.dfs(node, seen)