# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pre =[0] * len(s)
        ans = []
        for start ,end , direction in shifts:
            if direction == 0:
                pre[start] -= 1
                if end + 1 < len(s):
                    pre[end + 1] += 1
            else :
                pre[start] += 1
                if end + 1 < len(s):
                    pre[end + 1] -= 1
        for i in range(1,len(pre)):
            pre[i] += pre[i-1]
        
         
        for i in range(len(s)):
            print((ord(s[i]) + pre[i]) % 26)
            ans.append(ord('a') + ((ord(s[i]) - ord('a') + pre[i]) % 26)) 

        return "".join(chr(i) for i in ans)
            

                   