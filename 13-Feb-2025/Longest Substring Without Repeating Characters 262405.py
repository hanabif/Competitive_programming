# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        myset = set()
        ans = 0 
        for right in range(len(s)):
           
            while s[right] in myset:
                myset.remove(s[left])
                left+=1
            myset.add(s[right])
            ans=max(ans , len(myset))
        return ans

