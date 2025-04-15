# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = deque()
        moves = [[0,1],[1,0],[-1,0],[0,-1]]
        time , fresh = 0, 0
        ROWS, COLS = len(grid) , len(grid[0])

        def inbound(row,col):
            return  0 <= row < ROWS and 0 <= col < COLS 

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    que.append([i,j])
        
        while que and fresh > 0:
            for i in range(len(que)):
                r,c = que.popleft()
                for x,y in moves:
                    nr, nc = x + r, y + c
                    if not inbound(nr,nc) or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    que.append([nr,nc])
                    fresh -= 1
            time +=1
        if fresh == 0:
            return time
        else:
            return -1
