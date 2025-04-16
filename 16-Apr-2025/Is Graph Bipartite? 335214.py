# Problem: Is Graph Bipartite? - https://leetcode.com/problems/is-graph-bipartite/

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1] * len(graph)
        que = deque()

        for i in range(len(graph)):
            if color[i] == -1:
                color[i] = 0
                que.append(i)
                
            while que:
                node = que.popleft()
                for nbr in graph[node]:
                    if color[nbr] == -1:
                        color[nbr] = 1 - color[node]
                        que.append(nbr)
                    elif color[nbr] == color[node]:
                        return False
        return True
    

        
