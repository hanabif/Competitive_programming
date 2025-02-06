# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            for i in range(len(mat)):
                for j in range(i, len(mat)):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
                
            for row in mat:
                row.reverse()
            if mat==target:
                return True
        return False
        

        