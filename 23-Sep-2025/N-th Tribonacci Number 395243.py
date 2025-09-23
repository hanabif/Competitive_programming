# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    @cache
    def tribonacci(self, n: int) -> int:
        memo = {}
        if n == 0 or n == 1:
            return n
        if n == 2:
            return 1
        if n not in memo:
            memo[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
        return memo[n]