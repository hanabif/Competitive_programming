# Problem: Solving Questions With Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, que: List[List[int]]) -> int:
        

        dp = [0] * (len(que) + 1)
        for i in range(len(que) - 1, -1 , -1):
            skip = dp[i + 1]
            next_index = i + que[i][1] + 1
            take = que[i][0]
            if next_index < len(que):
                take = dp[next_index] + que[i][0]
            dp[i] = max(skip,take)
        return dp[0]