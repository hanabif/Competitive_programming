# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        r = len(grid)
        c = len(grid[0])
        def dp(i,j):
            if i == r - 1 and j == c - 1:
                return grid[i][j]
            if i >= r or j >= c:
                return float('inf')
            
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i,j)] = min(dp(i + 1,j), dp(i , j + 1)) + grid[i][j]
            
            return memo[(i,j)]
        return dp(0,0)
