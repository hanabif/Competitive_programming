# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        def inbound(i , j):
            return (0 <= i < rows and 0 <= j < cols)
        
        def dfs(row, col):
            board[row][col] = "*"
    
            visited.add((row,col))
            for dr,dc in directions:
                nr = row + dr
                nc = col + dc
                if inbound(nr,nc) and board[nr][nc] == "O":
                    dfs(nr,nc)
                
        for i in range(rows):
            for j in range(cols):
                if i !=0 and j != 0 and i != rows - 1 and j != cols - 1:
                    continue
                if board[i][j] == 'O':
                    dfs(i,j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == '*':
                    board[i][j] = 'O'
                else:
                    board[i][j] = 'X'

        

