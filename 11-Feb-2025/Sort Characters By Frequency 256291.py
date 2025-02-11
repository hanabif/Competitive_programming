# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        freq=Counter(s)
        ans=""
        
        freq=sorted(freq.items(),key=lambda item:item[1],reverse=True)
        for key,value in freq:
            ans+=key*value
        return ans

       