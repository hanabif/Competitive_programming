# Problem: House Robber II - https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        nums1 = nums[1:]
        nums2 = nums[:len(nums) - 1]

        memo1 = {}
        def dp1(i):
            if i == 0:
                return nums1[i]
            if i == 1:
                return max(nums1[1], nums1[0])
            if i not in memo1:
                memo1[i] = max(dp1(i - 1), dp1(i-2) + nums1[i])
            return memo1[i]
        
        memo2 = {}
        def dp2(i):
            if i == 0:
                return nums2[i]
            if i == 1:
                return max(nums2[0], nums2[1])
            if i not in memo2:
                memo2[i] = max(dp2(i - 1), dp2(i-2) + nums2[i])
            return memo2[i]
        
        return max(dp1(len(nums1) - 1), dp2(len(nums2) - 1))
