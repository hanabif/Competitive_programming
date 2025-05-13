# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        ROW = len(grid)
        COL = len(grid[0])
        visited = [[False for _ in range(COL)] for _ in range(ROW)]

        directions = {
            1: [((0, -1), [1, 4, 6]), ((0, 1), [1, 3, 5])],  
            2: [((-1, 0), [2, 3, 4]), ((1, 0), [2, 5, 6])],  
            3: [((0, -1), [1, 4, 6]), ((1, 0), [2, 5, 6])],  
            4: [((0, 1), [1, 3, 5]), ((1, 0), [2, 5, 6])],   
            5: [((0, -1), [1, 4, 6]), ((-1, 0), [2, 3, 4])], 
            6: [((0, 1), [1, 3, 5]), ((-1, 0), [2, 3, 4])]   
        }
        
        def inbound(i, j):
            return 0 <= i < ROW and 0 <= j < COL


        def dfs(r,c):
            if r == ROW - 1 and c == COL - 1:
                return True
            visited[r][c] = True
            for (x,y), nbr in directions[grid[r][c]]:
                nr , nc = x + r, y + c
                if inbound(nr,nc) and not visited[nr][nc]:
                    if grid[nr][nc] in nbr:
                        if dfs(nr,nc):
                            return True
            return False
        return dfs(0,0)