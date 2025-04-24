# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        Graph = defaultdict(list)
        out =  [0 for _ in range(len(graph))]
        for i in range(len(graph)):
            for j in graph[i]:
                Graph[j].append(i)
                out[i] += 1
        
        que = deque()
        for i in range(len(graph)):
            if out[i] == 0:
                que.append(i)
        
        ans = []
        while que:
            node = que.popleft()
            ans.append(node)

            for nbr in Graph[node]:
                out[nbr] -= 1
                if out[nbr] == 0 :
                    que.append(nbr)
        ans.sort()
        return ans
        


