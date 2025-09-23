# Problem: Longest Increasing Subsequence - https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [1] * n
        def dp(i):
            if i == n:
                return 0
            for j in range(i):
                if nums[i] > nums[j]:
                    memo[i] = max(memo[i] , memo[j] + 1)
           
            return memo[i]

        ans = float('-inf')
        for i in range(n):
            ans = max(ans,dp(i))
            
        return ans