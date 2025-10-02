# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        dp =[ [0] * (len(s) + 1) for _ in range(n + 1)]
        maxlen = 1
        start = 0
        for i in range(n):
            dp[i][i] = 1
            if i + 1 < n and s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                maxlen = 2
                start = i

        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n):
                if s[i] == s[j] and dp[i+1][j - 1]:
                    dp[i][j] = 1
                    if abs(i - j) + 1 > maxlen:
                        maxlen = abs(i - j) + 1  
                        start = i
        
        return s[start:start + maxlen]
            
        
            
            