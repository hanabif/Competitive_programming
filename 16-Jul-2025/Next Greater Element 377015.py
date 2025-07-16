# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, n1: List[int], n2: List[int]) -> List[int]:
        stack = []
        index = {}
        ans = [-1] * len(n1)

        for i, n in enumerate(n1):
            index[n] = i
        
        for n in n2:
            while stack and n > stack[-1]:
                if stack:
                    val = stack.pop()
                ans[index[val]] = n
            if n in n1:
                stack.append(n)
        return ans

