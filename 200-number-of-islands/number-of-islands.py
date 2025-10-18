class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        def dfs(pos):
            x, y = pos
            current = grid[x][y]
            if current == "#" or current == "0":
                return False
            grid[x][y] = "#"

            for x_offset, y_offset in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                new_x, new_y = x+x_offset, y+y_offset
                if 0 <= new_x < m and 0 <= new_y < n:
                    dfs((new_x, new_y))
            return True

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    if dfs((i, j)):
                        res += 1
        return res