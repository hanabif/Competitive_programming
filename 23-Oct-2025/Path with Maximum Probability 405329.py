# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(list)
        for(a,b), w in zip(edges, succProb):
            graph[a].append( [b,w])
            graph[b].append( [a,w])

        distances = defaultdict(lambda : float("-inf"))
        distances[start] = 1
        processed = set()
        heap = [(-1, start)]
        while heap:
            current_distance, current_node = heapq.heappop(heap)
            if current_node in processed:
                continue
            processed.add(current_node)

            for child, weight in graph[current_node]:
                distance = -current_distance * weight
                if distance > distances[child]:
                    distances[child] = distance
                    heapq.heappush(heap, (-distance, child))
        return distances[end] if distances[end] != float('-inf') else 0
        