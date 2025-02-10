# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row,col=len(mat),len(mat[0])
        i,j=0,0
        go_up=True
        res=[]
        
        while len(res)<row*col :
            if go_up:
                while i>=0 and j<col and i<row:
                    res.append(mat[i][j])
                    
                    i-=1
                    j+=1
                if j==col:
                    i+=2
                    j-=1
                else:
                    i+=1
                go_up=False
            else:
                while col>j>=0 and i<row:
                    res.append(mat[i][j])
                    
                    i+=1
                    j-=1
                if i==row:
                    i-=1
                    j+=2
                else:
                    j+=1
                go_up=True
        return(res)

