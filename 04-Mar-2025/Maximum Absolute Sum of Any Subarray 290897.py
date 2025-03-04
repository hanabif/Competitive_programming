# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        min_pre, max_pre = 0,0
        cur = 0
        res = 0

        for n in nums:
            cur+=n
            res = max(res, abs(cur - min_pre), abs(cur - max_pre))
            min_pre = min(cur,min_pre)
            max_pre = max(cur,max_pre)
        return res
        