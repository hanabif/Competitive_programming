# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subsets = []
        def dfs(i):
            if i == len(nums):
                res.append(subsets.copy())
                return
            
            subsets.append(nums[i])
            dfs(i + 1)

            subsets.pop()
            dfs(i + 1)
        dfs(0)
        return res

        
      

        