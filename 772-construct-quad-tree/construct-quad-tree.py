"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: list[list[int]]) -> 'Node':
        n = len(grid)
        def build(r, c, l):
            v = grid[r][c]
            for i in range(r, r+l):
                for j in range(c, c+l):
                    if grid[i][j] != v:
                        h = l//2
                        tl = build(r, c, h)
                        tr = build(r, c+h, h)
                        bl = build(r+h, c, h)
                        br = build(r+h, c+h, h)
                        return Node(True, False, tl, tr, bl, br)
            return Node(bool(v), True, None, None, None, None)
        return build(0, 0, n)