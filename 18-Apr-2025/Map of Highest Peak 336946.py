# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        que = deque()
        moves = [[0,1],[1,0],[-1,0],[0,-1]]
        ROWS, COLS = len(isWater) , len(isWater[0])
        height = [[-1 for _ in range(COLS)] for _ in range(ROWS)]

        def inbound(row,col):
            return  0 <= row < ROWS and 0 <= col < COLS 

        for i in range(ROWS):
            for j in range(COLS):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    que.append((i,j))
        
        while que:
          
            for i in range(len(que)):
                r,c = que.popleft()
                for x,y in moves:
                    nr, nc = x + r, y + c
                    if inbound(nr,nc) and height[nr][nc] == -1:
                        height[nr][nc] = height[r][c] + 1
                        que.append((nr,nc))
        return height
               