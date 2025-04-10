# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for i in range(len(manager)):
            graph[manager[i]].append(i)

        ans = 0
        def dfs(node, time):
            nonlocal ans
            ans = max(ans,time)
            for emp in graph[node]:
                dfs(emp, informTime[node] + time)

        dfs(headID, 0)
        return ans
           

