# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, can: List[int], target: int) -> List[List[int]]:
        res = []
        def back(i , store, summ):
            if summ == target: 
                res.append(store[:])
                return 
            if summ > target:
                return
            for j in range(i , len(can)):
                store.append(can[j])
                summ += can[j]
                back(j, store, summ)
                num = store.pop()
                summ-= num
        back(0 , [], 0)
        return res
        