# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = {}
        r = len(matrix)
        c = len(matrix[0])
        def dp(i,j):
            if i >= r or j < 0 or j >= c:
                return float('inf')
            if i == r - 1 :
                return matrix[i][j]          
            if (i, j) in memo:
                return memo[(i, j)]
            memo[(i,j)] =  min(dp(i + 1,j), dp(i + 1,j + 1), dp(i + 1,j - 1)) + matrix[i][j]
            return memo[(i,j)]
            
        ans = float('inf')
        for j in range(c):
            ans = min(ans,dp(0,j))
        return ans

