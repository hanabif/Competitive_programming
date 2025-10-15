# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prereq: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(list)
        for pre, crs in prereq:
            adj[crs].append(pre)


        def dfs(crs):
            if crs not in preMap:
                preMap[crs]= set() 
                for prereq in adj[crs]:
                    preMap[crs] |= dfs(prereq)
                preMap[crs].add(crs)
            return preMap[crs]
        
        preMap = {}
        for crs in range(numCourses):
            dfs(crs)
        
        res = []
        for u, v in queries:
            if u in preMap[v]:
                res.append(True)
            else:
                res.append(False)
        return res
