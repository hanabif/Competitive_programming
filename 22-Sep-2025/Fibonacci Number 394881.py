# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        memo = defaultdict(int)
        def helper(n):    
            if n == 1 or n == 0:
                return n
            if n not in memo:
                memo[n] = helper(n - 1) + helper(n - 2)

            return memo[n]
        return helper(n)