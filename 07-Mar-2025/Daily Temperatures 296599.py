# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temp)

        for i, num in enumerate(temp):
            while stack and temp[stack[-1]] < num:
                low = stack.pop()
                ans[low] = abs( i - low)
            else:
                stack.append(i)
        return ans


