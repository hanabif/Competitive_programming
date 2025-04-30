# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = -1 * grid[i][j]
            heapq.heapify(grid[i])

        heap = []
        for i in range(len(grid)):
            take = min(limits[i],len(grid[i]))
            for _ in range(take):
                val = heapq.heappop(grid[i])
                heapq.heappush(heap,val)
        
        ans = 0
        while k and heap:
            num = heapq.heappop(heap)
            ans += num
            k -= 1
        return -ans

        

        