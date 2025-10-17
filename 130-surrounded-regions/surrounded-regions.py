class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def dfs(pos: tuple, safe: set):
            i, j = pos

            if board[i][j] != "O":
                return

            for i_off, j_off in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                row, col = i+i_off, j+j_off
                if 0 <= row < m and 0 <= col < n:
                    if board[row][col] == "O" and (row, col) not in safe:
                        safe.add((row, col))
                        dfs((row, col), safe)

        safe = set()
        for i in range(m):
            if board[i][0] == "O":
                dfs((i, 0), safe)
                safe.add((i, 0))
            if board[i][n-1] == "O":
                dfs((i, n-1), safe)
                safe.add((i, n-1))
        for j in range(n):
            if board[0][j] == "O":
                dfs((0, j), safe)
                safe.add((0, j))
            if board[m-1][j] == "O":
                dfs((m - 1, j), safe)
                safe.add((m - 1, j))

        for i in range(1, m-1):
            for j in range(1, n-1):
                if (i, j) not in safe:
                    board[i][j] = "X"