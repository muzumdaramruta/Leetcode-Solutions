from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or board[i][j] == 'X':
                return
            
            visited[i][j] = True
            
            "Explore neighbors " 
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        "1. **Traverse** borders and mark connected 'O's"
        for j in range(n):
            "Top row"
            if board[0][j] == 'O' and not visited[0][j]:
                dfs(0, j)
            "Bottom row"
            if board[m - 1][j] == 'O' and not visited[m - 1][j]:
                dfs(m - 1, j)
        
        for i in range(m):
            "Left column"
            if board[i][0] == 'O' and not visited[i][0]:
                dfs(i, 0)
            "Right column"
            if board[i][n - 1] == 'O' and not visited[i][n - 1]:
                dfs(i, n - 1)

        "2. **Flip** unvisited 'O's"
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and not visited[i][j]:
                    board[i][j] = 'X'