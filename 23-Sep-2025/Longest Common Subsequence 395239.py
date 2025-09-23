# Problem: Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:
        memo = {}
        def dp(i,j):
            if i >= len(t1) or j >= len(t2):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
                
            if t1[i] == t2[j]:
                memo[(i,j)] = dp(i + 1,j + 1) + 1
            else:
                memo[(i,j)] = max(dp(i + 1,j), dp(i,j + 1))
            return memo[(i,j)]
        return dp(0,0)
