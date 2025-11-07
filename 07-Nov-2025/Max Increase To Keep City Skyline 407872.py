# Problem: Max Increase To Keep City Skyline - https://leetcode.com/problems/max-increase-to-keep-city-skyline/

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        rowMax = []
        colMax = []
        
        for row in grid:
            rowMax.append(max(row))
       
        for col in zip(*grid):
            colMax.append(max(col))

        ans = 0
        for i in range(n):
            for j in range(m):
                ans += abs(grid[i][j] - min(rowMax[i], colMax[j]))
        return ans
                
        