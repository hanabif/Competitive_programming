# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row=set("qwertyuiop")
        second_row=set("asdfghjkl")
        third_row=set("zxcvbnm")
        res=[]
        for word_in in words:
            word=set(word_in.lower())
            if word<=first_row or word<=second_row or word<=third_row:
                res.append(word_in)
        return res

