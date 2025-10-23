# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distance: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        for i, j, w in edges:
            dist[i][j] = dist[j][i] = w

        for i in range(n):
            dist[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        nbr = {}
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and dist[i][j] <= distance:
                    count += 1
                nbr[i] = count
        
        mini = min(nbr.values())
        ans = float('-inf')
        for city,nbrs in nbr.items():
            if nbrs == mini:
                ans = max(ans,city)

        return ans


        