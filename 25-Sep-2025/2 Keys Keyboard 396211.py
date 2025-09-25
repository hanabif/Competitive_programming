# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:
        memo = {}
        def dp(i,letter):
            if i == n:
                return 0
            if i > n:
                return float('inf')
            if (i,letter) in memo:
                return memo[(i,letter)]

            copy = dp(i + i, i) + 2
            paste = float('inf')
            if letter:
                paste = dp (i + letter, letter ) + 1
            memo[(i,letter)] = min(copy,paste)
            return memo[(i,letter)]
        return dp(1,0)
        