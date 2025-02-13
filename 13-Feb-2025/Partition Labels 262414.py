# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last={}
        for index , char in enumerate(s):
            last[char] = index
        
        size , ending = 0 , 0
        res = []

        for index , char in enumerate(s):
            size+=1
            ending = max ( ending , last[char] )
            
            if index == ending:
                res.append(size)
                size = 0
        return res


        