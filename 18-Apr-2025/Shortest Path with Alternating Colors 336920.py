# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n: int, red: List[List[int]], blue: List[List[int]]) -> List[int]:
        redG = defaultdict(list)
        blueG = defaultdict(list)

        for u,v in red:
            redG[u].append(v)
        for u,v in blue:
            blueG[u].append(v)
        
        ans = [-1] * n
        visited = set()
        que = deque()
        que.append((0,'blue',0))
        que.append((0,'red',0))

        while que:
            node, color, steps = que.popleft()
            if ans[node] == -1:
                ans[node] = steps
            else:
                ans[node] = min(ans[node], steps)

            if (node,color) in visited:
                continue
            visited.add((node,color))
            if color == 'red':
                for nbr in blueG[node]:
                    if (nbr, 'blue') not in visited:
                        que.append((nbr, 'blue', steps + 1))
            else:  
                for nbr in redG[node]:
                    if (nbr, 'red') not in visited:
                        que.append((nbr, 'red', steps + 1))

        return ans