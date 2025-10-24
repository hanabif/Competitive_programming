# Problem: Number of Restricted Path from First to Last Node - https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        distances = [float('inf')] * (n + 1)
        distances[n] = 0
        heap = [(0, n)]

        while heap:
            cost, node = heapq.heappop(heap)
            if cost > distances[node]:
                continue
            for nbr, w in graph[node]:
                new_cost = cost + w
                if new_cost < distances[nbr]:
                    distances[nbr] = new_cost
                    heapq.heappush(heap, (new_cost, nbr))

        nodes = list(range(1, n + 1))
        nodes.sort(key=lambda x: distances[x])

        
        dp = [0] * (n + 1)
        dp[n] = 1  

        for node in nodes:
            for nbr, _ in graph[node]:
                if distances[node] > distances[nbr]:
                    dp[node] = (dp[node] + dp[nbr]) % MOD

        return dp[1]
        