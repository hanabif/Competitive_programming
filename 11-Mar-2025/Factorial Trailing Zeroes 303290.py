# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def fact(n):
            if n <= 1:
                return 1
            return n * fact(n - 1)
        
        res = fact(n)
        count = 0
        while res > 0:
            if res %10 == 0:
                count+=1
                res //= 10
            else:
                break
        return count
