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
    def construct(self, grid: List[List[int]]) -> 'Node':
        if all(cell == grid[0][0] for row in grid for cell in row): return Node(bool(grid[0][0]), True)
        return Node(True, False, self.construct([row[:len(grid) // 2] for row in grid[:len(grid) // 2]]), self.construct([row[len(grid) // 2:] for row in grid[:len(grid) // 2]]), self.construct([row[:len(grid) // 2] for row in grid[len(grid) // 2:]]), self.construct([row[len(grid) // 2:] for row in grid[len(grid) // 2:]]))