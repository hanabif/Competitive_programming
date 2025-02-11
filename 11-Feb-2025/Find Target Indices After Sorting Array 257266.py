# Problem: Find Target Indices After Sorting Array - https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ans=[]
        for index,num in enumerate(nums):
            if nums[index]==target:
                ans.append(index)
        return ans
        