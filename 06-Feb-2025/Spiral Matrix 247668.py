# Problem: Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, num: List[List[int]]) -> List[int]:
        top,right,bottom,left=0,len(num[0])-1,len(num)-1,0
        ans=[]
       
        while top<=bottom and right>=left:
            
                # left to right
            temp=left
            while temp<=right:
                new=num[top][temp]
                temp+=1
                ans.append(new)
            top+=1

            # top to bottom

            temp=top
            while temp<=bottom:
                new=num[temp][right]
                temp+=1
                ans.append(new)
            right-=1
            
            # right to left
            if top<=bottom:
                temp=right
                while temp>=left:
                    new=num[bottom][temp]
                    temp-=1
                    ans.append(new)
                bottom-=1

            # bottom to top
            if right>=left:
                temp=bottom
                while temp>=top:
                    new=num[temp][left]
                    temp-=1
                    ans.append(new)
                left+=1
        return ans
            



        