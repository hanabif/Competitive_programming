# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i: [] for i in range(n)}
        for a,b,w in flights:
            graph[a].append( [b,w])
            
        heap = [(0, src, 0)] 
        distances = {(src, 0): 0}
        while heap:
            cost, node, stops = heapq.heappop(heap)
            if node == dst:
                return cost
            if stops > k:
                continue

            for neighbor, weight in graph[node]:
                new_cost = cost + weight  
                if (neighbor, stops + 1) not in distances or new_cost < distances[(neighbor, stops + 1)]:
                    distances[(neighbor, stops + 1)] = new_cost
                    heapq.heappush(heap, (new_cost, neighbor, stops + 1))
        return -1
        