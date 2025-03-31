# Problem: Generate Parentheses - https://leetcode.com/problems/generate-parentheses/description/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def back(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            if openN < n :
                stack.append("(")
                back(openN + 1, closeN)
                stack.pop()
            if closeN < openN:
                stack.append(")")
                back(openN , closeN + 1)
                stack.pop()
        back(0,0)
        return res

