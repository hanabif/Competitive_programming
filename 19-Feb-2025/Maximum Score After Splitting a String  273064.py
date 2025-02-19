# Problem: Maximum Score After Splitting a String  - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        s = list(map(int,s))
        total_ones = s.count(1)  
        left_zeros = 0
        right_ones = total_ones
        max_score = float('-inf')

        for i in range(len(s) - 1):
            if s[i] == 0:
                left_zeros += 1
            else:
                right_ones -= 1  
            
            
            max_score = max(max_score, left_zeros + right_ones)

        return max_score
            

            
        