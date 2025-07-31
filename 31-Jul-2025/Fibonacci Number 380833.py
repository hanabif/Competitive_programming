# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        ans = 0
        if n == 1:
            return 1
        if n == 0:
            return 0
        ans = self.fib(n-1) + self.fib(n - 2)
        return ans

        