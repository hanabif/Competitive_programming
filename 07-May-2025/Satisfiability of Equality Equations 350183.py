# Problem: Satisfiability of Equality Equations - https://leetcode.com/problems/satisfiability-of-equality-equations/

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent.setdefault(x, x)
            parent.setdefault(y, y)
            parent[find(x)] = find(y)

       
        for eq in equations:
            if eq[1] == '=':
                union(eq[0], eq[3])

       
        for eq in equations:
            if eq[1] == '!':
                parent.setdefault(eq[0], eq[0])
                parent.setdefault(eq[3], eq[3])
                if find(eq[0]) == find(eq[3]):
                    return False

        return True
