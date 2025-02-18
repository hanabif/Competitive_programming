# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        black_balls = []
        for i, char in enumerate(s):
            if char == '1':
                black_balls.append(i)
        
        k = len(black_balls)
        n = len(s)

        target = []
        for i in range(k):
            target.append(n-k+i)   
        
        swaps = 0
        for i in range(k):
            swaps += abs(target[i] - black_balls[i])
        return swaps