# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        letters = []
        for i in range(len(s)):
            if s[i].isalpha():
                letters.append(i)
        
        n = len(letters)
        res = []    
        for mask in range(1<<n):
            ans = list(s)
            for i in range(n):
                ind = letters[i]
                if (mask >> i) & 1:
                    ans[ind] = ans[ind].upper()
                else:
                    ans[ind] = ans[ind].lower()
            res.append("".join(ans))
        return res
