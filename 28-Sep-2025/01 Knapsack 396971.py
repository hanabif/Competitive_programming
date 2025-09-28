# Problem: 01 Knapsack - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

class Solution:
    def knapsack(self, W, val, wt):
        # code here
        dp = [[-1]*(W+1) for _ in range(len(val))]
        def recur(i ,w):
            if w <= 0 or i >= len(wt):
                return 0
                
            include = 0
            if dp[i][w] == -1:
                if w >= wt[i]:
                    include = recur(i+1 , w - wt[i]) + val[i]
                exclude = recur(i+1,w)
                dp[i][w] = max(include,exclude)
            return dp[i][w]
        return recur(0,W)