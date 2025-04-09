# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(list)

        for i in range(n):
            for j in range(i + 1,len(isConnected[i])):
                if isConnected[i][j] == 1:
                    graph[i + 1].append(j + 1)
                    graph[j + 1].append(i + 1)

        visited = set()
        def dfs(node):
            nonlocal visited
            visited.add(node)
            for i in graph[node]:
                if i not in visited:
                    dfs(i)
        count = 0
        for i in range(1 ,n + 1):
            if i not in visited:
                dfs(i)
                count += 1
        return count
