# Problem: Vowels of All Substrings - https://leetcode.com/problems/vowels-of-all-substrings/

class Solution:
    def countVowels(self, word: str) -> int:
        vowels = set("aeiou")
        n = len(word)
        total = 0
        
        for i, ch in enumerate(word):
            if ch in vowels:
                total += (i + 1) * (n - i)
        
        return total