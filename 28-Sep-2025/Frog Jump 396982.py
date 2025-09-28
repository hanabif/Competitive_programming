# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_set = set(stones)
        last_stone = stones[-1]
        memo = {}
        def dp(i,last):
            if i == last_stone:
                return True
            if (i,last) in memo:
                return memo[(i,last)]
            
            if last == 0:
                next_jumps = [1]
            else:
                next_jumps = [last - 1, last, last + 1]

            for next_jump in next_jumps:
                if next_jump > 0:
                    next_pos = i + next_jump
                    if next_pos in stone_set:
                        if dp(next_pos,next_jump):
                            memo[(i,last)] = True
                            return True                   
            memo[(i,last)] = False
            return False
        
        return dp(0,0)
            

