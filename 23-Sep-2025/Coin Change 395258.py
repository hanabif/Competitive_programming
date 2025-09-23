# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return float('inf')
            if rem in memo:
                return memo[rem]
            res = float('inf')
            for coin in coins:
                res = min(res,dp(rem - coin) + 1 ) 
                memo[rem] = res
            return res

        ans = dp(amount)
        if ans == float('inf'):
            return -1
        else:
            return ans

            
            