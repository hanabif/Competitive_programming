# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.append(-1)
        i = 0
        while i < len(nums):
            c = nums[i] 
            if c == -1:
                i +=1
            elif c != i:
                nums[i] , nums[c]=  nums[c], nums[i]
            else:
                i += 1
        return nums.index(-1)
    
        
