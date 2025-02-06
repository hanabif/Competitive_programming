# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        double=Counter(nums)
        ans=[]
        
        for i in double:
            if double[i]==2:
                ans.append(i)
        return ans