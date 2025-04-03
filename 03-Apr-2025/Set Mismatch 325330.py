# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        ans = []
        while i < n:
            c = nums[i] - 1
            if nums[i] == nums[c]:
                i += 1
            elif c != i:
                nums[c], nums[i] = nums[i], nums[c]
            else:
                i += 1
        
        for i in range(n):
            if nums[i] != i + 1:
                ans.append(nums[i])
                ans.append(i + 1)
                # break
        return ans