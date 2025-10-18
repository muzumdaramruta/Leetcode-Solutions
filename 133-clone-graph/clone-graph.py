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
            
        visited = {node: Node(val=node.val)}
        st = [node]
        
        while st:
            src = st.pop()
            copy = visited[src]
            for n in src.neighbors:
                if n not in visited:
                    visited[n] = Node(val=n.val)
                    st.append(n)
                copy.neighbors.append(visited[n])
        
        return visited[node]