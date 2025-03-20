# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def back(i, store):
            if len(store) == k:
                res.append(store.copy())
                return

            for i in range(i, n + 1):
                store.append(i)
                back(i + 1, store)
                store.pop()

        back(1, [])
        return res
