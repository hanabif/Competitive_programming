# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows , cols = len(matrix) , len(matrix[0])
        self.sum_mat=[[0]*(cols+1) for r in range(rows+1)]
       
        for r in range(rows):
            for c in range(cols):
                self.sum_mat[r+1][c+1] = (
                    matrix[r][c] +
                    self.sum_mat[r+1][c] +   
                    self.sum_mat[r][c+1] -   
                    self.sum_mat[r][c]       
                )


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1,col1,row2,col2=row1+1,col1+1,row2+1,col2+1

        
        bottomRight=self.sum_mat[row2][col2]
        above=self.sum_mat[row1-1][col2]
        left=self.sum_mat[row2][col1-1]
        topLeft= self.sum_mat[row1-1][col1-1]

        return bottomRight-above-left+topLeft


        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)