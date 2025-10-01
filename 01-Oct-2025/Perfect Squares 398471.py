# Problem: Perfect Squares - https://leetcode.com/problems/perfect-squares/

class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}
        def dp(rem):
            if rem == 0:
                return 0
            if rem in memo:
                return memo[rem]

            ans = float('inf')
            for sqr in range(1, int(rem**0.5) + 1):
                ans = min(ans, 1 + dp(rem - sqr * sqr))
            memo[rem] = ans
            return memo[rem]
        return dp(n)