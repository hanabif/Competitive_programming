# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        rev_graph = defaultdict(list)
        for u,v in edges:
            rev_graph[v].append(u)
        
        def dfs(node, visited):
            for nbr in rev_graph[node]:
                if nbr not in visited:
                    visited.add(nbr)
                    dfs(nbr,visited)
        ans = []
        for i in range(n):
            visited = set()
            dfs(i,visited)
            ans.append(sorted(visited))
        return ans
       