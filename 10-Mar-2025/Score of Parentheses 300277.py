# Problem: Score of Parentheses - https://leetcode.com/problems/score-of-parentheses/

class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        for p in s:
            if p =="(":
                stack.append(p)
            else:
                if stack[-1] == "(":
                    stack.pop()
                    stack.append(1)
                else:
                    num = 0
                    while stack and stack[-1] !="(":
                        num += stack.pop()
                    stack.pop()
                    stack.append(num*2)
        
        return sum(stack)
        
            
