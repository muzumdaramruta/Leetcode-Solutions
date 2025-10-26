from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        m,n=len(board),len(board[0])
        grid=dict()
        value=1
        board.reverse()
        t=0
        for i in range(0,m):
            for j in range(0,n):
                if(t%2==0):
                    grid[value]=board[i][j] if board[i][j]!=-1 else value
                else:
                    grid[value]=board[i][n-j-1] if board[i][n-j-1]!=-1 else value
                value+=1
            t+=1
        value-=1
        queue=deque()
        queue.append((1,0))
        while(queue):
            index,c=queue.popleft()
            for r in range(1,7):
                if(index+r in grid and grid[index+r]!=0):
                    if(grid[index+r]==value):
                        return c+1
                    queue.append((grid[index+r],c+1))
                    grid[index+r]=0
        return -1