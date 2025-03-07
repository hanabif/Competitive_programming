# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []
        for ch in s:
            if ch!="#":
                stack1.append(ch)
            else:
                if stack1:
                    stack1.pop()
                else:
                    stack1 = []
        for ch2 in t:
            if ch2!="#":
                stack2.append(ch2)
            else:
                if stack2:
                    stack2.pop()
                else:
                    stack2 = []
        if stack1 == stack2:
            return True
        else:
            return False




        