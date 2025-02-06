# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)

        ans = 0
        for word in words:
            c = Counter(word)
            isGood = True
            for key in c:
                if key not in count or count[key] < c[key]:
                    isGood = False
                    break
            if isGood:
                ans += len(word)
        return ans 


        