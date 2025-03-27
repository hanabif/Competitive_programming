# Problem: Find Minimum in Rotated Sorted Array  - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        mini = nums[0]
        l = 0
        r = len(nums) - 1
        while l<=r:
            mid = (l + r) // 2
            if nums[mid] >= mini:
                l = mid + 1    
            else:
                mini = nums[mid]
                r = mid - 1
        return mini
        