# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(math.sqrt(c))
        summ = 0
        while left <= right:
            summ = left**2 + right**2
            if summ == c:
                return True
            elif summ > c:
                right-= 1
            else:
                left+= 1
        return False
            
            

        