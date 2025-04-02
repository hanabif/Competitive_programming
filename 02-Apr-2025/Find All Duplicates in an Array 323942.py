# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        while i < len(nums):
            correct_index = nums[i] - 1 
            if nums[i] != nums[correct_index]: 
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] - 1 != i:
                ans.append(nums[i])
        return list(set(ans))

        