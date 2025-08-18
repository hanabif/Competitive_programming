# Problem: Maximum Number of Vowels in a Substring of Given Length - https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o','u']

        l , count, ans = 0,0,0
        for r in range(len(s)):
            if s[r] in vowels:
                count += 1
            if r - l + 1 > k:
                if s[l] in vowels:
                    count -= 1
                l += 1
            ans = max(ans,count)
        return ans

    