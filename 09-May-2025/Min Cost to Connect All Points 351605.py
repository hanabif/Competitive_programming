# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parent = [i for i in range(n)]
        size = [1 for _ in range(n)]

        def find(x):
            if parent[x] == x:
                return parent[x]
            parent[x] = find(parent[x])
            return parent[x]

        def union(a,b):
            parA = find(a)
            parB = find(b)
            if parA != parB:
                if size[parA] > size[parB]:
                    parent[parB] = parent[parA]
                    size[parA] += size[parB]
                else:
                    parent[parA] = parent[parB]
                    size[parB] += size[parA]
        
        distance = []
        for i in range(n):
            x1 , y1 = points[i]
            for j in range(i + 1, n):
                x2,y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                distance.append([dist,i,j])
        
        distance.sort()
        ans = 0
        for w,u,v in distance:
            if find(u) == find(v):
                continue
            union(u,v)
            ans += w
        return ans
