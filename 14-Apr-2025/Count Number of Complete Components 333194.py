# Problem: Count Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, ans):
            if node in visited:
                return 
            visited.add(node)
            ans.append(node)
            for nbr in graph[node]:
                dfs(nbr,ans)
            return ans
        
        res = 0
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            comp = dfs(i,[])
            if all((len(comp) - 1 == len(graph[i]) for i in comp)):
                res += 1
        return res