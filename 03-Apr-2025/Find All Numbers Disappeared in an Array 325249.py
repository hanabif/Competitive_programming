# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        while i < n:
            c = nums[i] - 1
            if nums[i] == nums[c]:
                i += 1
            elif c != i:
                nums[c], nums[i] = nums[i], nums[c]
            else:
                i += 1
        ans = []
        for i in range(n):
            if nums[i] != i + 1:
                ans.append(i + 1)
        return ans
