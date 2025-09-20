# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(i):
            self.visited.add(i)
            for j in range(len(isConnected)):
                if isConnected[i][j] and j not in self.visited:
                    dfs(j)
        
            return
        
        self.visited = set()
        province = 0
        for i in range(len(isConnected)):
            if i not in self.visited:
                province += 1
                dfs(i)
        return province