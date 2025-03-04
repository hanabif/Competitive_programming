# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = nums[0]
        n = len(nums)
        if n == 1: 
            return True
        
        for i in range(n):
            jump = max(jump, nums[i])
            if jump <= 0:
                return False
            if i + jump >= n - 1:
                return True
            jump-=1
        return False
        