# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        ROW2, COL2 = ROWS * 3 , COLS * 3
        grid2 = [[0] * COL2 for _ in range (ROW2)]

        for i in range(ROWS):
            for j in range(COLS):
                i2, j2 = i * 3, j * 3
                if grid[i][j] == "/":
                    grid2[i2][j2+2] = 1
                    grid2[i2+1][j2+1] = 1
                    grid2[i2+2][j2] = 1
                if grid[i][j] == '\\':
                    grid2[i2][j2] = 1
                    grid2[i2+1][j2+1] = 1
                    grid2[i2+2][j2+2] = 1

        def dfs(r,c,visited):
            if (r < 0 or c < 0 or r == ROW2 or c == COL2) or grid2[r][c] != 0 or (r,c) in visited:
                return 
            visited.add((r,c))
            nbr = [[r + 1, c], [r, c + 1], [r - 1, c],[r, c - 1]]

            for a,b in nbr:
                if (a,b) not in visited:
                    dfs(a,b,visited)
                    
        visited = set()
        ans = 0
        for i in range(ROW2):
            for j in range(COL2):
                if grid2[i][j] == 0  and (i,j) not in visited:
                    dfs(i,j,visited)
                    ans += 1
        return ans
            



