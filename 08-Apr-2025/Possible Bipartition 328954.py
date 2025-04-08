# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i,j in dislikes:
            graph[i].append(j)
            graph[j].append(i)
        
        color = [-1] * (n + 1)
        answer = True

        def dfs(node,col):
            nonlocal answer
            mycolor = 1-col
            color[node] = mycolor

            for nbr in graph[node]:
                if color[nbr] == -1:
                    dfs(nbr,mycolor)
                else:
                    if color[nbr] == mycolor:
                        answer = False

        
        for i in range(1,n + 1):
            if color[i] == -1:
               dfs(i,0)
        return answer
        

