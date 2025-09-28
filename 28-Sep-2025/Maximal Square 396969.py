# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        memo = {}
        def dp(i,j):
            if i >= row or j >= col:
                return 0
            
            if (i,j) in memo:
                return memo[(i,j)]
    
            memo[(i,j)] = 0
            down = dp(i + 1,j)
            right = dp(i, j + 1)
            diag = dp(i + 1, j + 1)
            if matrix[i][j] == '1':
                memo[(i,j)] = 1 + min(right,down,diag)
            return memo[(i,j)]
        dp(0,0)
        return max(memo.values()) ** 2
