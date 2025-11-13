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
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        def buildQuadTree(size, grid, startRow, startCol):
            if size == 1:
                return Node(bool(grid[startRow][startCol]), True)

            countZero = 0
            countOne = 0
            for row in range(startRow, startRow + size):
                for col in range(startCol, startCol + size):
                    if grid[row][col] == 1:
                        countOne += 1
                    else:
                        countZero += 1

            if countOne == size * size:
                return Node(True, True)
            elif countZero == size * size:
                return Node(False, True)
            else:
                halfSize = size // 2
                topLeftNode = buildQuadTree(halfSize, grid, startRow, startCol)
                topRightNode = buildQuadTree(halfSize, grid, startRow, startCol + halfSize)
                bottomLeftNode = buildQuadTree(halfSize, grid, startRow + halfSize, startCol)
                bottomRightNode = buildQuadTree(halfSize, grid, startRow + halfSize, startCol + halfSize)
                return Node(True, False, topLeftNode, topRightNode, bottomLeftNode, bottomRightNode)

        n = len(grid)
        if n == 0:
            return None

        return buildQuadTree(n, grid, 0, 0)