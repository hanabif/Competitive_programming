# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        decr = deque()
        incr = deque()
        left = 0
        ans = 0

        for right in range(len(nums)):
            while decr and nums[right] > decr[-1]:
                decr.pop()
            decr.append(nums[right])

            while incr and nums[right] < incr[-1]:
                incr.pop()
            incr.append(nums[right])

            while decr[0] - incr[0] > limit:
                if decr[0] == nums[left]:
                    decr.popleft()
                if incr[0] == nums[left]:
                    incr.popleft()
                left+=1
            ans = max(ans, right - left + 1)
        return ans