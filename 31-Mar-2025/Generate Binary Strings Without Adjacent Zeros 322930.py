# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        res=[]
        def back(index,store):
            if index == n:
                res.append(store)
                return
    
            if not store or store[-1] == "1":
                back(index + 1 , store + "0")
            back(index + 1 , store + "1")
             
        back(0 , "")
        return res