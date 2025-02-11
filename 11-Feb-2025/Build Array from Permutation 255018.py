# Problem: Build Array from Permutation - https://leetcode.com/problems/build-array-from-permutation/description/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans=[]
        index=defaultdict(int)
        for i in range(len(nums)):
            index[i]=nums[i]
        for i in range(len(nums)):
            ans.append(index[nums[i]])
        return ans
        
        