# Problem: Find Pivot Index - https://leetcode.com/problems/find-pivot-index/description/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pref = []  
        acc = 0
        for n in nums:
            acc += n
            pref.append(acc)
        
        suff = [0]*len(nums)  
        acc = 0
        for i in range(len(nums) - 1,-1,-1):
            acc += nums[i]
            suff[i] = acc

        ans = -1
        for i in range(len(nums)):
            if pref[i] == suff[i]:
                ans = i
                break
        return ans
        
