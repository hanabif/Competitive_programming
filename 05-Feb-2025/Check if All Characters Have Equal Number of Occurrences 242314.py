# Problem: Check if All Characters Have Equal Number of Occurrences - https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/description/

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        Hash=Counter(s)
        myset=set()
        for value in Hash.values():
            myset.add(value)
        if len(myset)!=1:
            return False
        return True
        
        
        