# Problem: Longest Arithmetic Subsequence  - https://leetcode.com/problems/longest-arithmetic-subsequence/

class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [dict() for _ in range(n)]
        longest = 0

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[j].get(diff, 1) + 1
                longest = max(longest, dp[i][diff])

        return longest
