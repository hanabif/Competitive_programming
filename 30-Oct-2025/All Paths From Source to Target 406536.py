# Problem: All Paths From Source to Target - https://leetcode.com/problems/all-paths-from-source-to-target/

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        def backtrack(i,stack):
            if i == len(graph)-1:
                res.append(stack[:])
                return
            if i >= len(graph):
                return
            
            for n in graph[i]:
                stack.append(n)
                backtrack(n,stack)
                stack.pop()
        backtrack(0,[0])
        return res