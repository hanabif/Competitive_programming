# Problem: Minimum Cost to Convert String I - https://leetcode.com/problems/minimum-cost-to-convert-string-i/description/?envType=problem-list-v2&envId=shortest-path

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        graph = defaultdict(list)
        for src,dst, cur_cost in zip(original, changed, cost):
            graph[src].append((dst,cur_cost))

        def dijkstra(src):
            heap = [(0,src)]
            mini_cost_map = {}

            while heap:
                cost, node = heapq.heappop(heap)
                if node in mini_cost_map:
                    continue
                mini_cost_map[node] = cost
                for nbr, nbr_cost in graph[node]:
                    heapq.heappush(heap ,(cost + nbr_cost, nbr) ) 
            return  mini_cost_map

        mini_cost_maps = { c: dijkstra(c) for c in set(source)}
            
        res = 0
        for s , t  in zip(source , target):
            if t not in mini_cost_maps[s]:
                return -1
            res += mini_cost_maps[s][t]
        return res