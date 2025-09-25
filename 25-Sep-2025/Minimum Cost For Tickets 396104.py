# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        n = len(days)
        def dp(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            
            j = i
            while j < n and days[j] < days[i] + 1:
                j += 1
            oneday = dp(j) + costs[0]

            j = i
            while j < n and days[j] < days[i] + 7:
                j += 1
            sevday = dp(j) + costs[1]

            j = i
            while j < n and days[j] < days[i] + 30:
                j += 1
            thirday = dp(j) + costs[2]

            memo[i] = min(oneday, sevday,thirday)
            return memo[i]
            
        return dp(0)