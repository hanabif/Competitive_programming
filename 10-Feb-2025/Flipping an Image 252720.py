# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            i=i.reverse()
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j]==1:
                    image[i][j]=0
                else:
                    image[i][j]=1
        return image
                    
        