# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        bitmask = 0
        ans = 0
        for right in range(len(nums)):
            while bitmask & nums[right]:
                bitmask ^= nums[left]
                left += 1
            bitmask |= nums[right]
            ans = max(ans,right - left + 1)
        return ans