# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(i):
            if i == 0 or i == 1:
                return 1
            if i not in memo:
                memo[i] = dp(i -1) + dp(i - 2)
            return memo[i]
        return dp(n)
        
