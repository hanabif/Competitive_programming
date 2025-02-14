# Problem: Largest Number - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        ans=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]<nums[j]+nums[i]:
                    nums[i],nums[j]=nums[j],nums[i]

        ans="".join(nums)
        if ans[0]=="0":
            return "0"
        return ans

                