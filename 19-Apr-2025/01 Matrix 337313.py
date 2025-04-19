# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        que = deque()
        moves = [[0,1],[1,0],[-1,0],[0,-1]]
        ROWS, COLS = len(mat) , len(mat[0])
        dist = [[float('inf')] * COLS for _ in range(ROWS)]

        for i in range(ROWS):
            for j in range(COLS):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    que.append((i,j))
        
        def inbound(row,col):
            return  0 <= row < ROWS and 0 <= col < COLS
        
        visited = set()
        while que:
            x,y = que.popleft()
            if (x,y) in visited:
                continue
            visited.add((x,y))
            for r,c in moves:
                nx = x + r
                ny = y + c
                if inbound(nx,ny) and dist[nx][ny] > dist[x][y] + 1:
                    dist[nx][ny] = dist[x][y] + 1
                    que.append((nx,ny))
        return dist

