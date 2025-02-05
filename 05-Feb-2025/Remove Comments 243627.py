# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans=[]
        is_block_comment=False
        new_line=[]
        for line in source:
            i=0
            while i<len(line):
                if not is_block_comment:
                    if line[i:i+2]=="//":
                        break
                    elif line[i:i+2]=="/*":
                        i+=1
                        is_block_comment=True
                    else:
                        new_line.append(line[i])
                else:
                    if line[i:i+2]=="*/":
                        i+=1
                        is_block_comment=False
                i+=1
            if not is_block_comment and new_line:
                ans.append("".join(new_line))
                new_line=[]
        return ans
                
            