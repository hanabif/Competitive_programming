# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        dist = {node: float('inf') for node in range(1, n + 1)}
        dist[k] = 0
        processed = set()

        heap = [(0, k)]
        while heap:
            current_time, current_node = heapq.heappop(heap)
            if current_node in processed:
                continue
            processed.add(current_node)

            for child, weight in graph[current_node]:
                time = current_time + weight
                if time < dist[child]:
                    dist[child] = time
                    heapq.heappush(heap, (time, child))
        maxi = max(dist.values())
        if maxi == float('inf'):
            return -1
        else:
            return maxi