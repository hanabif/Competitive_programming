# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n=len(matrix)
        ans=[]
        for i in range(len(matrix[0])):
            temp=[]
            for j in range(n):
                temp.append(matrix[j][i])
            ans.append(temp)
        return ans
            
   
        