# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        que = deque()
        moves = [[0,1],[1,0],[-1,0],[0,-1]]
        ROWS, COLS = len(image) , len(image[0])

        if image[sr][sc] == color:
            return image

        def inbound(row,col):
            return  0 <= row < ROWS and 0 <= col < COLS

        start = image[sr][sc]
        que = deque()
        que.append((sr,sc))

        while que:
            row,col = que.popleft()
            image[row][col] = color
            for x,y in moves:
                nrow = row + x
                ncol = col + y
                if inbound(nrow,ncol) and image[nrow][ncol] == start:
                    que.append((nrow,ncol))
        return image
