# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        que = deque()
        moves = [[0,1],[1,0],[-1,0],[0,-1],[-1,-1],[-1,1],[1,-1],[1,1]]
        ROWS, COLS = len(board) , len(board[0])

        cr = click[0]
        cc = click[1]
       
        if board[cr][cc] == 'M':
            board[cr][cc] = 'X'
            return board
        
        def inbound(row,col):
            return  0 <= row < ROWS and 0 <= col < COLS  

        que.append((cr,cc))
        visited = set()
        while que:
            for _ in range(len(que)):
                count = 0
                row, col = que.popleft()
                for dr,dc in moves:
                    nr = row + dr
                    nc = col + dc
                    if inbound(nr,nc) and board[nr][nc] == 'M':
                        count += 1
                if count > 0:
                    board[row][col] = str(count)
                else:
                    board[row][col] = 'B'
                    for dr,dc in moves:
                        nr = row + dr
                        nc = col + dc
                        if inbound(nr,nc) and (nr,nc) not in visited:
                            visited.add((nr,nc))
                            que.append((nr,nc))
                    
        return board
        






        