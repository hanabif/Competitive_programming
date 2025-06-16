# Problem: Checking Existence of Edge Length Limited Paths - https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]  # path compression
            x = self.parent[x]
        return x
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        self.parent[py] = px
        return True

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda x: x[2])
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1][2])

        uf = UnionFind(n)
        res = [False] * len(queries)

        i = 0 
        for idx, (u, v, limit) in sorted_queries:
            while i < len(edgeList) and edgeList[i][2] < limit:
                uf.union(edgeList[i][0], edgeList[i][1])
                i += 1
            if uf.find(u) == uf.find(v):
                res[idx] = True
        
        return res
        