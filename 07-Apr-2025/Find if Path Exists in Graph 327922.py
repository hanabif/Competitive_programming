# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        found = False
        def dfs(ver, visited):
            nonlocal found
            if ver == destination:
                found = True
            
            visited.add(ver)
            for child in graph[ver]:
                if child not in visited:
                    dfs(child,visited)
                
        dfs(source,set([]))
        return found


        