# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        for node in employees:
            graph[node.id].extend((node.id, node.importance, node.subordinates))
        
        def dfs(i):
            id, imp, nbr = graph[i][0] , graph[i][1], graph[i][2]
            ans = imp

            if not nbr:
                return ans
            for n in nbr:
                ans += dfs(n)
            return ans
        return dfs(id)
            
            



