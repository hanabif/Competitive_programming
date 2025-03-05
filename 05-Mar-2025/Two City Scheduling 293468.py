# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = 0
        costs.sort(key = lambda x: (x[0] - x[1]))
        res+=sum(costs[i][0] for i in range(len(costs)//2 ))
        res+=sum(costs[i][1] for i in range(len(costs)//2,len(costs)))
        return res