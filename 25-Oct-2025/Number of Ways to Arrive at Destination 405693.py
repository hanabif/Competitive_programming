# Problem: Number of Ways to Arrive at Destination - https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v,t in roads:
            graph[u].append([t,v])
            graph[v].append([t,u])

        MOD = 10 ** 9 + 7
        heap = [(0,0)]
        distances = [float('inf')] * n
        path = [0] * n
        path[0] = 1

        while heap:
            cost, node = heappop(heap)

            for nbr_cost, nbr in graph[node]:
                new = cost + nbr_cost
                if new < distances[nbr]:
                    distances[nbr] = new
                    path[nbr] = path[node]
                    heappush(heap, (new, nbr))
                elif new == distances[nbr]:
                    path[nbr] = (path[nbr] + path[node]) % MOD
        return path[n - 1]
