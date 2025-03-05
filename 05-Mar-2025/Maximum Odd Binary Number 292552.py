# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = list(s)
            
        ones = s.count('1')

        i = 0
        for _ in range(ones - 1):
            s[i] = '1'
            i +=1
        
        for j in range(i , len(s) - 1):
            s[j] = '0'

        s[-1] ='1'
        return "".join(s)