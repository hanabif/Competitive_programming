# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        in_deg = [0] * n 
        for u,v in edges:
            in_deg[v] += 1

        ans = -1
        for i in range(n):
            if in_deg[i] == 0:
                if ans == -1:
                    ans = i
                else:
                    return -1
        return ans
       