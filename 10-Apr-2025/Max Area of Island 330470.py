# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()


        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0 or (row,col) in visited:
                return 0
            visited.add((row,col))
            ans = 1
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                ans += dfs(new_row, new_col) 
            return ans

        area = 0
        for i in range(rows):
            for j in range(cols):
                area = max(area, dfs(i,j))
        return area

