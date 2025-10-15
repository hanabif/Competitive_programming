# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [set() for _ in range(n)]

        for i , j in edges:
            adj[i].add(j)
            adj[j].add(i)
        if n == 1 :
            return [0]

        qu = deque(i for i in range(n) if len(adj[i]) == 1 )
        remain = n

        while remain > 2 :
            remain -= len(qu)
            for _ in range(len(qu)):
                curr = qu.popleft()
                for child in adj[curr]:
                    adj[child].remove(curr)
                    if len(adj[child]) == 1:
                        qu.append(child)
        
                
        return list(qu)
            
