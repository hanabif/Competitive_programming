# Problem: Baseball Game
 (Easy) - https://leetcode.com/problems/baseball-game/

class Solution:
    def calPoints(self, ope: List[str]) -> int:
        stack = []
        for o in ope:
            if o == 'C':
                if stack:
                    stack.pop()
            elif o == "D":
                stack.append(stack[-1] * 2)
            elif o == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(o))
        return sum(stack)