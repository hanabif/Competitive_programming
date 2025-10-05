# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        memo = {}
        def dp(i,j):
            if i > j:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            
            if (j - 1 )% 2 :
                even = True
            else:
                even = False
            
            left = piles[i] if even else 0
            right = piles[j]  if even else 0

            memo[(i,j)] = max(dp(i + 1,j) + left , dp(i, j - 1) + right)
            return memo[(i,j)]
        return dp(0, len(piles) - 1) > (sum(piles)) // 2