class Solution(object):
    def construct(self, grid):
        def create(x, y, n):
            node = Node()
            t = grid[x][y]
            for i in range(x, x+n):
                for j in range(y, y+n):
                    if grid[i][j] != t:
                       node.topLeft = create(x, y, n//2)
                       node.topRight = create(x, y+ n//2, n//2 )
                       node.bottomLeft = create(x+ n//2, y, n//2)
                       node.bottomRight = create(x+ n//2, y+ n//2, n//2)
                       return node
            node.isLeaf = True
            node.val = t
            return node
        return create(0, 0, len(grid))