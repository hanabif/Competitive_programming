# Problem: Word Break - https://leetcode.com/problems/word-break/description/

class Solution:
    def wordBreak(self, s: str, word: List[str]) -> bool:  
        word = set(word)
        memo = {}
        def dp(i):
            if i == len(s):
                return True    
            if i in memo:
                return memo[i]

            for j in range( i + 1 ,len(s) + 1):
                if s[i:j] in word and dp(j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        return dp(0)

